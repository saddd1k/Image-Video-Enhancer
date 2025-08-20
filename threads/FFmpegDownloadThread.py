from PySide6.QtCore import QThread, Signal
import pillow_heif
pillow_heif.register_heif_opener()
import urllib.request, io, zipfile, os

class FFmpegDownloadThread(QThread):
    finished = Signal(str)
    error = Signal(str)

    def run(self):
        try:
            url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
            data = urllib.request.urlopen(url).read()
            archive = zipfile.ZipFile(io.BytesIO(data))
            for name in archive.namelist():
                if name.endswith("ffmpeg.exe"):
                    dest = os.path.join(os.getcwd(), os.path.basename(name))
                    with open(dest, 'wb') as f:
                        f.write(archive.read(name))
                    self.finished.emit(dest)
                    return
            raise RuntimeError("ffmpeg.exe not found")
        except Exception as e:
            self.error.emit(str(e))