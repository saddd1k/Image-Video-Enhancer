from PySide6.QtCore import QThread, Signal
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
from realesrgan import RealESRGANer
from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan.archs.srvgg_arch import SRVGGNetCompact
import pillow_heif
pillow_heif.register_heif_opener()
import subprocess, re, shutil, tempfile, os

class VideoUpscaleThread(QThread):
    update_log = Signal(str)
    finished_all = Signal()
    error = Signal(str)
    file_done = Signal(str)

    def __init__(self, files, params, parent=None):
        super().__init__(parent)
        self.files = files
        self.params = params
        self.ffmpeg_path = params.get('ffmpeg_path', 'ffmpeg')
        self.current_lang = self.params.get('language', 'English')

    def log(self, msg):
        self.update_log.emit(msg)

    def run(self):
        temp_dir = tempfile.mkdtemp()
        try:
            device = self.params['device']
            scale = self.params['scale']
            model_name = self.params['model_name']
            output_folder = self.params['output_folder']
            format_ext = self.params['output_format'].lower()
            codec = self.params['codec']
            crf = self.params['crf']
            keep_fps = self.params['keep_fps']
            remove_audio = self.params['remove_audio']
            flags = self.params['flags']
            current_lang = self.current_lang
            if current_lang == "Русский":
                self.log(f"Апскейл: model_name={model_name!r}, scale={scale}, do_upscale={self.params['do_upscale']}")
            else:
                self.log(f"Upscale: model_name={model_name!r}, scale={scale}, do_upscale={self.params['do_upscale']}")
            for video_path in self.files:
                base_name = os.path.splitext(os.path.basename(video_path))[0]
                frame_pattern = os.path.join(temp_dir, f"frame_%06d.{format_ext}")
                if current_lang == "Русский":
                    self.log(f"Извлечение кадров из {video_path}...")
                else:
                    self.log(f"Extracting frames from {video_path}...")

                probe = subprocess.run(
                    [self.ffmpeg_path, '-i', video_path],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                fps = 30.0
                match = re.search(r'(\d+(?:\.\d+)?) fps', probe.stderr)
                if match:
                    fps = float(match.group(1)) if match else 30.0
                if current_lang == "Русский":
                    self.log(f"FPS исходного видео: {fps}")
                else:
                    self.log(f"FPS of the original video: {fps}")
                frame_pattern = os.path.join(temp_dir, f'frame_%06d.{format_ext}')
                if current_lang == "Русский":
                    self.log("Извлечение кадров...")
                else:
                    self.log("Extracting frames...")
                extract_cmd = [
                self.ffmpeg_path, '-i', video_path, '-vsync', '0'
                ]

                fmt = format_ext.lower()
                if fmt in ('jpg', 'jpeg'):
                    qscale = max(2, min(31, int(round((31 - 2) * (crf / 51.0) + 2))))
                    extract_cmd += ['-q:v', str(qscale)]
                elif fmt == 'webp':
                    webp_q = max(0, min(100, int(round(100 - (crf / 51.0) * 100))))
                    extract_cmd += ['-q:v', str(webp_q)]
                extract_cmd += [frame_pattern]
                subprocess.run(extract_cmd, check=True)
                frames = sorted(f for f in os.listdir(temp_dir) if f.startswith('frame_'))
                if current_lang == "Русский":
                    self.log(f"Кадры извлечены: {len(frames)} файлов")
                else:
                    self.log(f"Frames extracted: {len(frames)} files")
                if current_lang == "Русский":
                    self.log(f"Обнаружено {len(frames)} кадров.")
                else:
                    self.log(f"Detected {len(frames)} frames.")
                if self.params['do_upscale']:
                    model_path = os.path.join(self.params['model_dir'], model_name)
                    model_scale = scale
                    model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23,
                                    num_grow_ch=32, scale=scale)
                    if model_name == 'RealESRGAN_x4plus_anime_6B.pth':
                        model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=6,
                                        num_grow_ch=32, scale=4)
                        model_scale = 4
                    elif model_name in ('realesr-animevideov3.pth', 'realesr-animevideov3'):
                        model = SRVGGNetCompact(num_in_ch=3, num_out_ch=3, num_feat=64,
                                                num_conv=16, upscale=4, act_type='prelu')
                        model_scale = 4
                    upsampler = RealESRGANer(
                        scale=model_scale,
                        model_path=model_path,
                        model=model,
                        tile=256,
                        tile_pad=10,
                        pre_pad=0,
                        half = bool(self.params.get('half_precision', False)) and str(device).startswith('cuda'),
                        device=device
                    )
                    
                else:
                    upsampler = None
                for frame_name in frames:
                    frame_path = os.path.join(temp_dir, frame_name)
                    img = Image.open(frame_path)
                    alpha = None
                    if img.mode == "RGBA":
                        alpha = img.getchannel("A")
                        img = img.convert("RGB")
                    else:
                        img = img.convert("RGB")

                    
                    if upsampler:
                        img_np = np.array(img)[..., ::-1]
                        output, _ = upsampler.enhance(img_np, outscale=scale)
                        img = Image.fromarray(output[..., ::-1])
                    if alpha is not None:
                        img = img.convert("RGBA")
                        img.putalpha(alpha.resize(img.size, Image.LANCZOS))
                    flags = self.params['flags']
                    if flags.get('noice_remover'):
                        img = img.filter(ImageFilter.GaussianBlur(1))
                    if flags.get('better_colours'):
                        img = ImageEnhance.Color(img).enhance(1.2)
                    if flags.get('contrast_sharpness'):
                        img = ImageEnhance.Sharpness(img).enhance(2)
                    if flags.get('better_curcuits'):
                        img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
                    if flags.get('dehaze'):
                        img = ImageEnhance.Contrast(img).enhance(1.1)
                        img = ImageEnhance.Color(img).enhance(1.1)
                    if flags.get('jpeg_artifacts_remove'):
                        img = img.filter(ImageFilter.MedianFilter(3))
                        img = img.filter(ImageFilter.SHARPEN)
                    if flags.get('sepia'):
                        data = [(
                            min(int(0.393 * r + 0.769 * g + 0.189 * b), 255),
                            min(int(0.349 * r + 0.686 * g + 0.168 * b), 255),
                            min(int(0.272 * r + 0.534 * g + 0.131 * b), 255)
                        ) for r, g, b in img.getdata()]
                        img.putdata(data)
                    s = self.params.get('saturation', 1.0)
                    c = self.params.get('contrast', 1.0)
                    if s != 1.0:
                        img = ImageEnhance.Color(img).enhance(s)
                    if c != 1.0:
                        img = ImageEnhance.Contrast(img).enhance(c)
                    img.save(frame_path)
                current_lang = self.current_lang
                if current_lang == "Русский":
                    self.log("Собираем видео...")
                else:
                    self.log("Compiling video...")
                ext = os.path.splitext(video_path)[1].lower()
                is_gif = ext == '.gif'
                output_ext = 'gif' if is_gif else 'mp4'
                output_path = os.path.join(output_folder, f"{base_name}_out.{output_ext}")
                vcodec = {
                    'H.264 (AVC)': 'libx264',
                    'H.265 (HEVC)': 'libx265',
                    'AV1': 'libaom-av1'
                }.get(codec, 'libx264')

                frame_input = os.path.join(temp_dir, f"frame_%06d.{format_ext}")
                if keep_fps:
                    out_fps = fps
                else:
                    out_fps = max(fps, 30)
                cmd = [
                    self.ffmpeg_path,
                    '-y',
                    '-framerate', str(out_fps),
                    '-start_number', '1',
                    '-i', frame_input,
                ]
                vf_filters = ['pad=ceil(iw/2)*2:ceil(ih/2)*2']
                if self.params.get('remove_black_lines', False):
                    vf_filters.insert(0, 'crop=in_w:in_h-80:0:40')
                vf_filter_str = ','.join(vf_filters)

                if not is_gif:
                    cmd += ['-i', video_path]
                    if remove_audio:
                        cmd += [
                            '-c:v', vcodec,
                            '-pix_fmt', 'yuv420p',
                            '-vf', vf_filter_str,
                            '-r', str(out_fps),
                            '-movflags', '+faststart',
                            '-an'
                        ]
                    else:
                        cmd += [
                            '-map', '0:v:0',
                            '-map', '1:a:0?',
                            '-c:v', vcodec,
                            '-pix_fmt', 'yuv420p',
                            '-vf', vf_filter_str,
                            '-r', str(out_fps),
                            '-movflags', '+faststart',
                            '-c:a', 'copy'
                        ]
                    if isinstance(crf, (int, float)):
                        cmd += ['-crf', str(int(crf))]
                else:
                    cmd += ['-loop', '0']
                if self.params.get('remove_metainfo', False):
                    cmd += ['-map_metadata', '-1']
                cmd.append(output_path)
                subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                current_lang = self.current_lang
                if current_lang == "Русский":
                    self.log(f"Готово: {output_path}")
                else:
                    self.log(f"Done: {output_path}")
                self.file_done.emit(video_path)
            self.finished_all.emit()
        except Exception as e:
            self.error.emit(str(e))
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)