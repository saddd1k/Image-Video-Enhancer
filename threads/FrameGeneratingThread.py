import subprocess, re, shutil, tempfile, os, sys, torch
from PySide6.QtCore import QThread, Signal
from PIL import Image
import numpy as np
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'ECCV2022-RIFE')
BASE = os.path.normpath(BASE)
if BASE not in sys.path:
    sys.path.insert(0, BASE)
from model.RIFE import Model
from torchvision import transforms
import torch.nn.functional as F

class FrameGeneratingThread(QThread):
    update_log = Signal(str)
    finished_all = Signal()
    file_done = Signal(str)
    error = Signal(str)

    def __init__(self, files, params, parent=None):
        super().__init__(parent)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.rife_model = Model()
        self.rife_model.flownet.to(self.device)
        self.rife_model.lap.to(self.device)
        self.files = files
        self.params = params
        self.ffmpeg_path = params.get('ffmpeg_path', 'ffmpeg')
        self.current_lang = self.params.get('language', 'English')
        self.transform = transforms.Compose([transforms.ToTensor()])

    def log(self, msg):
        self.update_log.emit(msg)

    def tensor_to_pil(self, tensor):
        tensor = tensor.clamp(0,1)
        return transforms.ToPILImage()(tensor.cpu())

    def run(self):
        temp_dir = tempfile.mkdtemp()
        try:
            factor        = self.params['factor']
            output_folder = self.params.get('output_folder')
            frame_format  = self.params.get('frame_format', 'PNG')
            quality       = self.params.get('image_quality', 100)
            codec         = self.params.get('codec', 'H.264 (AVC)')
            video_format  = self.params.get('video_format', 'mp4')
            crf           = self.params.get('crf', 23)
            remove_black  = self.params.get('remove_black_lines', False)
            remove_meta   = self.params.get('remove_metainfo', False)
            remove_audio  = self.params.get('remove_audio', True)

            os.makedirs(output_folder, exist_ok=True)

            for video_path in self.files:
                base_name  = os.path.splitext(os.path.basename(video_path))[0]
                frames_dir = os.path.join(temp_dir, f"frames_{base_name}")
                out_dir    = os.path.join(temp_dir, f"out_{base_name}")
                os.makedirs(frames_dir, exist_ok=True)
                os.makedirs(out_dir,    exist_ok=True)
                if self.current_lang == "Русский":
                    self.log(f"Извлечение кадров из {video_path}...")
                else:
                    self.log(f"Extracting frames from {video_path}...")
                subprocess.run([
                    self.ffmpeg_path, '-i', video_path,
                    '-vsync', 'passthrough',
                    os.path.join(frames_dir, 'orig_%06d.png')
                ], check=True)
                probe = subprocess.run([
                    self.ffmpeg_path, '-i', video_path
                ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                m   = re.search(r"(\d+(?:\.\d+)?) fps", probe.stderr)
                fps = float(m.group(1)) if m else 30.0
                fps_out = round(fps * factor)
                files = sorted(f for f in os.listdir(frames_dir) if f.startswith('orig_'))
                fmt   = frame_format.split()[0].lower()
                ext   = 'jpg' if fmt=='jpeg' else fmt
                prepared = []
                if remove_black and files:
                    sample_idx = np.linspace(0, len(files)-1, num=min(7, len(files)), dtype=int)
                    tops, bottoms = [], []
                    for si in sample_idx:
                        a = np.array(Image.open(os.path.join(frames_dir, files[si])).convert('L'))
                        rows = (a > 10).any(axis=1)
                        nz = np.where(rows)[0]
                        if nz.size:
                            tops.append(nz[0])
                            bottoms.append(a.shape[0]-1 - nz[-1])
                    top_cut = int(np.median(tops)) if tops else 0
                    bottom_cut = int(np.median(bottoms)) if bottoms else 0
                else:
                    top_cut = bottom_cut = 0


                prepared = []
                for i, fname in enumerate(files, 1):
                    img = Image.open(os.path.join(frames_dir, fname)).convert('RGB')
                    if top_cut or bottom_cut:
                        img = img.crop((0, top_cut, img.width, img.height - bottom_cut))
                    if img.width % 2:
                        img = img.crop((0, 0, img.width - 1, img.height))
                    if img.height % 2:
                        img = img.crop((0, 0, img.width, img.height - 1))
                    outf = os.path.join(frames_dir, f"frame_{i:06d}.{ext}")
                    img.save(outf, quality=quality) if ext in ['jpg','webp'] else img.save(outf)
                    prepared.append(outf)

                if self.current_lang == "Русский":
                    self.log(f"Подготовлено {len(prepared)} кадров для интерполяции")
                    self.log("Интерполяция кадров...")
                else:
                    self.log(f"Prepared {len(prepared)} frames for interpolation")
                    self.log("Interpolating frames...")
                idx = 1
                for a, b in zip(prepared, prepared[1:]):
                    shutil.copy(a, os.path.join(out_dir, f"frame_{idx:06d}.{ext}")); idx += 1

                    t1 = self.transform(Image.open(a)).unsqueeze(0).to(self.device)
                    t2 = self.transform(Image.open(b)).unsqueeze(0).to(self.device)
                    H, W = t1.shape[2], t1.shape[3]
                    pad_h = (32 - H % 32) % 32
                    pad_w = (32 - W % 32) % 32
                    if pad_h or pad_w:
                        pad = (0, pad_w, 0, pad_h)
                        t1p = F.pad(t1, pad, mode='replicate')
                        t2p = F.pad(t2, pad, mode='replicate')
                    else:
                        t1p, t2p = t1, t2

                    for j in range(1, factor):
                        with torch.no_grad():
                            res_tensor = self.rife_model.inference(t1p, t2p, timestep=j / factor)
                        res_tensor = res_tensor[:, :, :H, :W]
                        out_img = self.tensor_to_pil(res_tensor.squeeze(0))
                        outf = os.path.join(out_dir, f"frame_{idx:06d}.{ext}")
                        out_img.save(outf, quality=quality) if ext in ['jpg','webp'] else out_img.save(outf)
                        idx += 1
                shutil.copy(prepared[-1], os.path.join(out_dir, f"frame_{idx:06d}.{ext}"))
                out_ext = 'gif' if video_format=='gif' else 'mp4'
                out_file = os.path.join(output_folder, f"{base_name}_out.{out_ext}")
                frame_input = os.path.normpath(os.path.join(out_dir, f"frame_%06d.{ext}"))
                output_file = os.path.normpath(out_file)
                video_input = os.path.normpath(video_path)

                cmd = [
                    self.ffmpeg_path,
                    '-y',
                    '-framerate', str(fps_out),
                    '-start_number', '1',
                    '-i', frame_input,
                ]

                is_video = os.path.splitext(video_path)[1].lower() in ['.mp4', '.avi', '.mov', '.mkv', '.webm']

                if remove_audio or not is_video:
                    cmd.append('-an')
                else:
                    cmd += [
                        '-i', video_input,
                        '-map', '0:v',
                        '-map', '1:a',
                        '-c:a', 'aac',
                        '-b:a', '320k',
                        '-shortest'
                    ]

                cmd += [
                    '-vf', 'pad=ceil(iw/2)*2:ceil(ih/2)*2:0:0,format=yuv420p',
                    '-c:v', {'H.264 (AVC)': 'libx264', 'H.265 (HEVC)': 'libx265', 'AV1': 'libaom-av1'}[codec],
                    '-preset', 'slow',
                    '-crf', str(crf),
                    '-r', str(fps_out),
                    '-movflags', '+faststart'
                ]

                if remove_meta:
                    cmd += ['-map_metadata', '-1']

                cmd.append(output_file)
                self.log("FFMPEG CMD: " + ' '.join(cmd))
                res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                self.log("FFMPEG STDERR:\n" + res.stderr)
                if res.returncode != 0:
                    if self.current_lang == "Русский":
                        self.log("Ошибка при выполнении FFmpeg")
                    else:
                        self.log("FFmpeg error")
                if self.current_lang == "Русский":
                    self.log(f"Готово: {out_file}")
                else:
                    self.log(f"Done: {out_file}")
                self.file_done.emit(video_path)
                shutil.rmtree(frames_dir, ignore_errors=True)
                shutil.rmtree(out_dir,    ignore_errors=True)

            self.finished_all.emit()
        except Exception as e:
            self.error.emit(str(e))
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)