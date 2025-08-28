from PySide6.QtCore import QThread, Signal
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import torch, os, sys
from realesrgan import RealESRGANer
from basicsr.archs.rrdbnet_arch import RRDBNet
import pillow_heif
pillow_heif.register_heif_opener()


class ImageUpscaleThread(QThread):
    file_done = Signal(str)
    finished_all = Signal()
    error = Signal(str)

    def __init__(self, files, params, parent=None):
        super().__init__(parent)
        self.files = files
        self.params = params
        self.current_lang = self.params.get('language', 'English')

    
    def normalize_format(self, fmt_str):
        if fmt_str is None:
            return None
        fmt_str = fmt_str.lower()
        if "png" in fmt_str:
            return "PNG"
        elif "jpeg" in fmt_str or "jpg" in fmt_str:
            return "JPEG"
        elif "webp" in fmt_str:
            return "WEBP"
        return fmt_str.upper()

    def run(self):
        try:
            device = self.params['device']
            md = self.params['model_dir']
            mn = self.params['model_name'] 
            sc = self.params['scale']
            model = None

            if self.params['do_upscale']:
                model_path = os.path.join(md, mn)
                arch = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64,
                               num_block=23, num_grow_ch=32, scale=sc)
                if mn == 'RealESRGAN_x4plus_anime_6B.pth':
                    arch = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64,
                                   num_block=6, num_grow_ch=32, scale=sc)
                model = RealESRGANer(
                    scale=sc,
                    model_path=model_path,
                    model=arch,
                    tile=256,
                    tile_pad=10,
                    pre_pad=0,
                    half=(device.type == 'cuda'),
                    device=device
                )

            for idx, fp in enumerate(self.files, 1):
                img = Image.open(fp)
                alpha = None

                if img.mode == "RGBA":
                    alpha = img.getchannel("A")
                    img = img.convert("RGB")
                else:
                    img = img.convert("RGB")
                arr = np.array(img)[..., ::-1]  # RGB -> BGR
                if self.params['do_upscale']:
                    out, _ = model.enhance(arr, outscale=sc)
                    img = Image.fromarray(out[..., ::-1])  # BGR -> RGB
                else:
                    out = arr
                    img = Image.fromarray(out[..., ::-1])  # BGR -> RGB
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
                saturation = self.params['saturation']
                contrast = self.params['contrast']
                if saturation != 1:
                    img = ImageEnhance.Color(img).enhance(saturation)
                if contrast != 1:
                    img = ImageEnhance.Contrast(img).enhance(contrast)
                out_format = self.normalize_format(self.params['output_format'])
                qual = self.params['quality']
                output_folder = self.params['output_folder']
                filename = os.path.splitext(os.path.basename(fp))[0]
                save_path = os.path.join(output_folder, f"{filename}_out.{out_format.lower()}")
                if out_format in ("JPEG", "WEBP"):
                    img.save(save_path, format=out_format, quality=qual)
                else:
                    img.save(save_path, format=out_format) 
                if device.type == 'cuda':
                    torch.cuda.empty_cache()
                self.file_done.emit(fp)
            self.finished_all.emit()

        except Exception as e:
            self.error.emit(str(e))
