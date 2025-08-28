from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QInputDialog, QButtonGroup
from PySide6.QtGui import QPixmap, QMovie, QIcon, QCloseEvent
from PySide6.QtCore import Qt, QTranslator, QCoreApplication
from PIL.ImageQt import ImageQt
from ui_widget import Ui_AI_processer
from PIL import Image
from presets import load_last_paths, load_presets, save_last_paths, save_presets
from pynvml import nvmlInit, nvmlDeviceGetHandleByIndex, nvmlDeviceGetMemoryInfo
from threads.ImageEnhancerThread import ImageUpscaleThread
from threads.VideoEnhancerThread import VideoUpscaleThread
from threads.FFmpegDownloadThread import FFmpegDownloadThread
from themes import *
import torch, os, sys, re, pywinstyles
from threads.FrameGeneratingThread import FrameGeneratingThread

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.model_dir = 'weights/'
        self.scroll_area_castle = scroll_area_castle
        self.orange_ffmpeg_path = orange_ffmpeg_path
        self.orange_ffmpeg_download = orange_ffmpeg_download 
        self.simple_red_sheet = simple_red_sheet
        self.red_sheet = red_sheet
        self.blue_sheet = blue_sheet
        self.blue_sheet_special = blue_sheet_special
        self.orange_sheet = orange_sheet
        self.choose_img_blue = choose_img_blue
        self.choose_img_orange = choose_img_orange
        self.setFixedSize(1171, 1023)
        self.translator = QTranslator()
        self.ui = Ui_AI_processer()
        self.ui.setupUi(self)
        self.current_lang = self.ui.language_comboBox.currentText()
        paths = load_last_paths()
        self.loaded_images = []
        self.loaded_videos = []
        self.loaded_interp_videos = []
        self.presets = load_presets()
        self.update_presets_list()
        self.upscale_thread = None
        self.scroll_content = QWidget()
        self.scroll_preview_layout = QVBoxLayout(self.scroll_content)
        self.scroll_preview_layout.setAlignment(Qt.AlignTop)
        self.ui.scrollArea.setWidget(self.scroll_content)
        self.ui.scrollArea.setWidgetResizable(True)
        self.ui.image_quality_spinBox.setEnabled(False)
        self.ui.image_quality_spinBox_2.setEnabled(False)
        self.ui.output_folder.setText(paths.get("output_folder_image", ""))
        self.ui.output_folder_lineEDIT.setText(paths.get("output_folder_video", ""))
        self.ui.ffmpeg_path_lineEDIT.setText(paths.get("ffmpeg_path", ""))  
        self.ui.output_folder_lineEDIT_3.setText(paths.get("output_folder_interpolate", ""))
        self.ui.ffmpeg_path_lineEDIT_2.setText(paths.get("ffmpeg_path", ""))
        self.ui.theme_pushButton.setChecked(paths.get("glass_mode", False))
        self.ui.language_comboBox.setItemData(0, "en_US")
        self.ui.language_comboBox.setItemData(1, "ru_RU")
        self.ui.language_comboBox.currentIndexChanged.connect(self.on_language_changed)
        lang_idx = paths.get("language", 0)
        self.ui.language_comboBox.setCurrentIndex(lang_idx)
        self.on_language_changed(lang_idx)
        self.theme_button_group = QButtonGroup(self)
        self.theme_button_group.addButton(self.ui.light_theme_radio)
        self.theme_button_group.addButton(self.ui.dark_theme_radio)
        self.theme_button_group.addButton(self.ui.castle_theme_radio)
        self.ui.choose_saving_folder_button.clicked.connect(self.choose_output_dir)
        self.ui.choose_images_button.clicked.connect(self.choose_files)
        self.ui.start_processing_button.clicked.connect(self.start_processing)
        self.ui.stop_processing_button.clicked.connect(self.stop_processing)
        self.ui.clear_button.clicked.connect(self.clear_images)
        self.ui.save_options_button.clicked.connect(self.save_current_preset)
        self.ui.remove_preset_button.clicked.connect(self.remove_selected_preset)
        self.ui.preset_comboBox.currentTextChanged.connect(self.apply_preset)
        self.ui.format_image_comboBox.currentTextChanged.connect(self.update_quality_spinbox_state)
        self.ui.input_video_button.clicked.connect(self.choose_videos)
        self.ui.output_folder_button.clicked.connect(self.choose_video_output_dir)
        self.ui.ffmpeg_path_button.clicked.connect(self.choose_ffmpeg_path)
        self.ui.ffmpeg_download_button.clicked.connect(self.start_ffmpeg_download)
        self.ui.start_processing_video_button.clicked.connect(self.start_processing_video)
        self.ui.stop_processing_video_button.clicked.connect(self.stop_processing)
        self.ui.clear_logs_button.clicked.connect(self.clear_logs)
        self.ui.format_image_comboBox_2.currentTextChanged.connect(self.update_quality_spinbox_state_2)
        self.ui.dark_theme_radio.clicked.connect(self.set_dark_theme)
        self.ui.light_theme_radio.clicked.connect(self.set_light_theme)
        self.ui.castle_theme_radio.clicked.connect(self.set_castle_theme)
        self.init_cuda_info()
        self.ui.cuda_update_pushButton.clicked.connect(self.init_cuda_info)
        self.ui.input_video_button_2.clicked.connect(self.choose_videos_to_interpolate)
        self.ui.output_folder_button_2.clicked.connect(self.choose_video_to_interpolate_output_dir)
        self.ui.ffmpeg_path_button_2.clicked.connect(self.choose_ffmpeg_path)
        self.ui.ffmpeg_download_button_2.clicked.connect(self.start_ffmpeg_download)
        self.ui.clear_frame_output_button.clicked.connect(self.clear_frames_logs)
        self.ui.stop_processing_frames_button.clicked.connect(self.stop_processing)
        self.ui.start_processing_frames_button.clicked.connect(self.start_frames_processing)
        self.ui.theme_pushButton.clicked.connect(self.init_glass_mode)
        self.ui.format_image_comboBox_4.currentTextChanged.connect(self.update_quality_spinbox_state_4)
        self.update_quality_spinbox_state_4(self.ui.format_image_comboBox_4.currentText())
        self.movie_i2 = QMovie(r"assets/I2_slomo_clipped.gif")
        self.movie_d2 = QMovie(r"assets/D2_slomo_clipped.gif")
        self.ui.gifLabelI2.setMovie(self.movie_i2)
        self.ui.gifLabelD2.setMovie(self.movie_d2)
        self.movie_i2.start()
        self.movie_d2.start()
        theme = paths.get("theme", "light")
        self.white = False
        if theme == "dark":
            self.ui.dark_theme_radio.setChecked(True)
            self.set_dark_theme()
        elif theme == "castle":
            self.ui.castle_theme_radio.setChecked(True)
            self.set_castle_theme()
        else:
            self.ui.light_theme_radio.setChecked(True)
            self.set_light_theme()

    def set_light_theme(self):
        self.set_dark_theme()
        if self.ui.quality_crf_label.text() == 'Качество/CRF (1-51):':
            self.ui.quality_crf_label.setText('Качество/CRF (0-51 для x264/x265, 1-51 для NVENC CQP):')
        if self.ui.quality_crf_label.text() == 'Quality/CRF (1-51):':
            self.ui.quality_crf_label.setText('Quality/CRF (0-51 for x264/x265, 1-51 for NVENC CQP):')
        self.setStyleSheet("""
QWidget {
    background-color: #F9F9F9;
    color: black;
    font-family: Segoe UI, sans-serif;
    font-size: 10pt;                      
            }

    QTabWidget::pane {
    border: 1px solid black;
    padding: 5px;
}

QTabBar::tab {
    border: 1px solid black;
    padding: 2px 5px;
    background: #F0F0F0;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
}

QTabBar::tab:selected {
    background: white;
    margin-bottom: -1px;
}

                           
QCheckBox {
    spacing: 6px;
}
                
QCheckBox::indicator:unchecked {
    background-color: transparent;
    border: 1px solid black;
    border-radius: 4px;
}

QCheckBox::indicator:checked {
    background-color: #7187D8;
    border: 2px solid #5365B5;
    border-radius: 4px;
}

QComboBox {
    border: 1px solid black;
    border-radius: 4px;
    padding: 5px 10px;
}

QComboBox::drop-down {
    width: 0px;
    border: none;
}

QComboBox::down-arrow {
    image: none;
    width: 0px;
    height: 0px;
}

QGroupBox {
    border: 1px solid black;
    border-radius: 5px;
    margin-top: 6px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 3px;
}
""")
        self.init_cuda_info()
        if self.ui.theme_pushButton.isChecked():
            self.white = True
            pywinstyles.apply_style(self, 'win7')
            pywinstyles.set_opacity(int(self.winId()), 0.8)
        
    def set_dark_theme(self):
        choose_img_blue = self.choose_img_blue
        if self.ui.quality_crf_label.text() == 'Качество/CRF:':
            self.ui.quality_crf_label.setText('Качество/CRF (0-51 для x264/x265, 1-51 для NVENC CQP):')
        if self.ui.quality_crf_label.text() == 'Quality/CRF:':
            self.ui.quality_crf_label.setText('Quality/CRF (0-51 for x264/x265, 1-51 for NVENC CQP):')
        scrollArea_dark = """
QScrollArea {
    border: 2px solid #5365B5;
    border-radius: 5px;
    padding: 5px 12px;
}
"""
        self.ui.scrollArea.setStyleSheet(scrollArea_dark)
        self.setStyleSheet("""
QWidget {
    background-color: #2E2E2E;
    color: #FFFFFF;
    font-family: Segoe UI, sans-serif;
    font-size: 10pt;
}
""")
        blue_sheet = self.blue_sheet
        simple_red_sheet = self.simple_red_sheet
        blue_sheet_special = self.blue_sheet_special
        current_lang = self.current_lang
        self.ui.stop_processing_button.setStyleSheet(simple_red_sheet)
        self.ui.clear_button.setStyleSheet(blue_sheet)
        self.ui.start_processing_button.setStyleSheet(blue_sheet)
        self.ui.save_options_button.setStyleSheet(blue_sheet)
        self.ui.remove_preset_button.setStyleSheet(blue_sheet)
        self.ui.choose_saving_folder_button.setStyleSheet(blue_sheet)
        self.ui.input_video_button.setStyleSheet(blue_sheet)
        self.ui.output_folder_button.setStyleSheet(blue_sheet)
        if current_lang == 'Русский':
            self.ui.ffmpeg_path_button.setStyleSheet(blue_sheet)
            self.ui.ffmpeg_download_button.setStyleSheet(blue_sheet)
            self.ui.ffmpeg_path_button_2.setStyleSheet(blue_sheet)
            self.ui.ffmpeg_download_button_2.setStyleSheet(blue_sheet)
        else:
            self.ui.ffmpeg_path_button.setStyleSheet(blue_sheet_special)
            self.ui.ffmpeg_download_button.setStyleSheet(blue_sheet_special)
            self.ui.ffmpeg_path_button_2.setStyleSheet(blue_sheet_special)
            self.ui.ffmpeg_download_button_2.setStyleSheet(blue_sheet_special)
        self.ui.start_processing_video_button.setStyleSheet(blue_sheet)
        self.ui.clear_logs_button.setStyleSheet(blue_sheet)
        self.ui.stop_processing_video_button.setStyleSheet(simple_red_sheet)
        self.ui.choose_images_button.setStyleSheet(choose_img_blue)
        self.ui.input_video_button_2.setStyleSheet(blue_sheet)
        self.ui.output_folder_button_2.setStyleSheet(blue_sheet)
        self.ui.start_processing_frames_button.setStyleSheet(blue_sheet)
        self.ui.clear_frame_output_button.setStyleSheet(blue_sheet)
        self.ui.theme_pushButton.setStyleSheet(blue_sheet)
        self.ui.stop_processing_frames_button.setStyleSheet(simple_red_sheet)
        self.init_cuda_info()
        if self.white and not self.ui.light_theme_radio.isChecked():
            if self.ui.theme_pushButton.isChecked():
                self.restart()
        if not self.white and not self.ui.light_theme_radio.isChecked():
            if self.ui.theme_pushButton.isChecked() and not self.ui.light_theme_radio.isChecked():
                pywinstyles.apply_style(self, 'aero')

    def set_castle_theme(self):
        self.ui.choose_images_button.setStyleSheet("""
QPushButton {
    background-color: transparent;
    color: #FF8C42;
    border: 2px dashed #FF8C42;
    border-radius: 5px;
    padding: 5px 12px
}

QPushButton:hover {
	background-color: transparent;
	color: #FFA35B;
	border: 2px dashed #FFA35B;
	border-radius: 5px;
    padding: 5px 12px
}

QPushButton:pressed {
	background-color: transparent;
	color: #CC6A1C;
	border: 2px dashed #CC6A1C;
	border-radius: 5px;
    padding: 5px 12px
}
                    """)

        self.setStyleSheet("""
QWidget {
    background-color: #000000;
    color: #FFFFFF;
    font-family: Cascadia Mono;
    font-size: 10pt;
}
        
QCheckBox {
    spacing: 6px;
    }

QCheckBox::indicator:unchecked {
    background-color: #444;
    border: 2px solid #777;
    border-radius: 4px;
}

QCheckBox::indicator:checked {
    background-color: #FF8C42;
    border: 2px solid #fc7a26;
    border-radius: 4px;
}
                    """)
        self.ui.ffmpeg_download_button.setStyleSheet(orange_ffmpeg_download)
        self.ui.ffmpeg_path_button.setStyleSheet(orange_ffmpeg_path)
        choose_img_orange = self.choose_img_orange
        if self.current_lang == 'Русский':
            self.ui.quality_crf_label.setText('Качество/CRF')
        else:
            self.ui.quality_crf_label.setText('Quality/CRF')
        orange_sheet = self.orange_sheet
        red_sheet = self.red_sheet
        scroll_area_castle = self.scroll_area_castle
        self.ui.scrollArea.setStyleSheet(scroll_area_castle)
        self.ui.stop_processing_button.setStyleSheet(red_sheet)
        self.ui.clear_button.setStyleSheet(orange_sheet)
        self.ui.start_processing_button.setStyleSheet(orange_sheet)
        self.ui.save_options_button.setStyleSheet(orange_sheet)
        self.ui.remove_preset_button.setStyleSheet(orange_sheet)
        self.ui.choose_saving_folder_button.setStyleSheet(orange_sheet)
        self.ui.input_video_button.setStyleSheet(orange_sheet)
        self.ui.output_folder_button.setStyleSheet(orange_sheet)
        self.ui.start_processing_video_button.setStyleSheet(orange_sheet)
        self.ui.clear_logs_button.setStyleSheet(orange_sheet)
        self.ui.stop_processing_video_button.setStyleSheet(red_sheet)
        self.ui.input_video_button_2.setStyleSheet(orange_sheet)
        self.ui.output_folder_button_2.setStyleSheet(orange_sheet)
        self.ui.ffmpeg_path_button_2.setStyleSheet(orange_ffmpeg_path)
        self.ui.ffmpeg_download_button_2.setStyleSheet(orange_ffmpeg_download)
        self.ui.start_processing_frames_button.setStyleSheet(orange_sheet)
        self.ui.clear_frame_output_button.setStyleSheet(orange_sheet)
        self.ui.theme_pushButton.setStyleSheet(orange_sheet)
        self.ui.stop_processing_frames_button.setStyleSheet(red_sheet)
        self.init_cuda_info()
        if self.white:
            if self.ui.theme_pushButton.isChecked():
                self.restart()
        elif self.ui.theme_pushButton.isChecked():
            pywinstyles.apply_style(self, 'aero')

    def restart_to_aero(self):
        if self.ui.theme_pushButton.isChecked():
            if self.white == True:
                pywinstyles.apply_style(self, 'aero')
                return QCoreApplication.exit(EXIT_CODE_REBOOT)  

    def restart(self):
        win7_theme_changer = False
        if not self.ui.theme_pushButton.isChecked() and self.ui.light_theme_radio.isChecked():
            win7_theme_changer = True
        if self.current_lang == 'Русский' and not win7_theme_changer:
            reply = QMessageBox.question(
                self,
                "Требуется перезагрузка программы.",
                "Хотите ли вы применить glass mode?",
                QMessageBox.Yes | QMessageBox.No,
                    )
        elif self.current_lang == 'English' and not win7_theme_changer:
            reply = QMessageBox.question(
                self,
                " Program Restart Required",
                "Would you like to apply glass mode?",
                QMessageBox.Yes | QMessageBox.No,
            )
        if self.current_lang == 'Русский' and win7_theme_changer:
            reply = QMessageBox.question(
                self,
                "Требуется перезагрузка программы.",
                "Хотите ли вы убрать nostalgic glass mode?",
                QMessageBox.Yes | QMessageBox.No,
            )
        elif self.current_lang == 'English' and win7_theme_changer:
            reply = QMessageBox.question(
                self,
                "Program Restart Required",
                "Would you like to remove nostalgic glass mode?",
                QMessageBox.Yes | QMessageBox.No,
            )
        if reply == QMessageBox.Yes:
            self.closeEvent(event=QCloseEvent())
            if not self.ui.light_theme_radio.isChecked():
                self.restart_to_aero()
            else:
                return QCoreApplication.exit(EXIT_CODE_REBOOT)

    def init_glass_mode(self):
        if self.ui.theme_pushButton.isChecked() and not self.ui.light_theme_radio.isChecked():
            pywinstyles.apply_style(self, 'aero')
        else:
            self.setStyleSheet('')
            if self.ui.castle_theme_radio.isChecked():
                self.set_castle_theme()
            elif self.ui.light_theme_radio.isChecked():
                self.set_light_theme()
            else:
                self.set_dark_theme()
            if not self.ui.theme_pushButton.isChecked() and self.ui.light_theme_radio.isChecked():
                self.restart()

    def get_current_theme(self):
        if self.ui.dark_theme_radio.isChecked():
            return "dark"
        elif self.ui.castle_theme_radio.isChecked():
            return "castle"
        else:
            return "light"

    def on_language_changed(self, index):
        app = QApplication.instance()
        app.removeTranslator(self.translator)

        if index == 0:
            if self.translator.load("translations/en_US.qm"):
                app.installTranslator(self.translator)
            self.current_lang = "English"
        elif index == 1:
            if self.translator.load("translations/ru_RU.qm"):
                app.installTranslator(self.translator)
            self.current_lang = "Русский"
        self.ui.retranslateUi(self)
        self.init_cuda_info()

    def init_cuda_info(self):
        layout = self.ui.cuda_info_widget.layout()
        if layout:
            for i in reversed(range(layout.count())):
                widget = layout.itemAt(i).widget()
                if widget:
                    widget.setParent(None)
        else:
            layout = QVBoxLayout(self.ui.cuda_info_widget)
            self.ui.cuda_info_widget.setLayout(layout)

        if not torch.cuda.is_available():
            self.ui.cuda_info_widget.setStyleSheet("""
            QWidget {
                border: 2px solid #633302;
                border-radius: 7px;
                padding: 5px 12px;
                background-color: transparent;
                    }
            QLabel {
                border: none;
                background-color: transparent;
                    }""")
            self.ui.model_status_badge_label.setText('❗')
            self.ui.model_status_badge_label.setStyleSheet("""
                QLabel {
                    background-color: black;
                    border: 1px solid #5365B5;
                    border-radius: 5px;
                    padding: 5px 12px;
                    font-size: 11pt;
    }
                        """)
            self.ui.model_status_label.setText(self.tr("Статус моделей: неактивный"))
            return
        elif torch.cuda.is_available():
            self.ui.cuda_info_widget.setStyleSheet("""
            QWidget {
            border: 2px solid #3B84A1;
            border-radius: 7px;
            padding: 5px 12px;
            background-color: transparent;
                    }
            QLabel {
                border: none;
                background-color: transparent;
                    }
            """)
            self.ui.model_status_badge_label.setText('💡')
            if self.ui.dark_theme_radio.isChecked():
                self.ui.model_status_badge_label.setStyleSheet("""
                QLabel {
            background-color: #5365B5;
            border: 1px solid #3345e8;
            border-radius: 5px;
            padding: 5px 12px;
            font-size: 11pt;
                    }
                    """)
            elif self.ui.light_theme_radio.isChecked():
                self.ui.model_status_badge_label.setStyleSheet("""
                QLabel {
            background-color: #525252;
            border: 1px solid yellow;
            border-radius: 5px;
            padding: 5px 12px;
            font-size: 11pt;
                    }
                    """)
            elif self.ui.castle_theme_radio.isChecked():
                self.ui.model_status_badge_label.setStyleSheet("""
                QLabel {
                        background-color: #FF8C42;
                        border: 1px solid yellow;
                        border-radius: 5px;
                        padding: 5px 12px;
                        font-size: 11pt;
                        }
        """)
            self.ui.model_status_label.setText(self.tr("Статус моделей: активный"))
            self.ui.cuda_status_label.setText(self.tr("Доступно"))
            self.ui.gp_cuda_info_label.setText(self.tr("Приложение будет использовать GPU (CUDA) для обработки"))
            f = self.ui.cuda_status_label.font(); f.setBold(True); self.ui.cuda_status_label.setFont(f)
            self.ui.cuda_status_label.setStyleSheet("color: #3A9940;")
            f = self.ui.gp_cuda_info_label.font(); f.setBold(True); self.ui.gp_cuda_info_label.setFont(f)
            self.ui.gp_cuda_info_label.setStyleSheet("color: #3A9940;")

            nvmlInit()
            device_count = torch.cuda.device_count()
            if self.current_lang == "Русский":
                self.ui.cuda_devices_label.setText(self.tr(f"Количество устройств: {device_count}"))
            else:
                self.ui.cuda_devices_label.setText(self.tr(f"Number of devices: {device_count}"))

            for i in range(device_count):
                name = torch.cuda.get_device_name(i)
                handle = nvmlDeviceGetHandleByIndex(i)
                mem = nvmlDeviceGetMemoryInfo(handle)
                allocated_gb = torch.cuda.memory_allocated(i) / 1e9
                cached_gb = torch.cuda.memory_reserved(i) / 1e9
                total_gb = mem.total / 1e9
                used_gb = mem.used / 1e9
                current_lang = self.current_lang
                if current_lang == "Русский" or current_lang == "Russian":
                    text = self.tr(
            f"GPU: {name} "
            f"(Всего VRAM: {total_gb:.1f} GB, "
            f"Занято: {used_gb:.1f} GB, "
            f"Выделено: {allocated_gb:.1f} GB, "
            f"Кэшировано: {cached_gb:.1f} GB)"  
        )
                elif current_lang == 'English' or current_lang == "Английский":
                    text = self.tr(
            f"GPU: {name} "
            f"(Total VRAM: {total_gb:.1f} GB, "
            f"Used: {used_gb:.1f} GB, "
            f"Allocated: {allocated_gb:.1f} GB, "
            f"Cached: {cached_gb:.1f} GB)"
        )
                lbl = QLabel(text, self.ui.cuda_info_widget)
                lbl.setStyleSheet("background-color: transparent;")
                layout.addWidget(lbl)
            return

    def closeEvent(self, event):
        save_last_paths(
            output_img=self.ui.output_folder.text(),
            output_vid=self.ui.output_folder_lineEDIT.text(),
            output_interpolate=self.ui.output_folder_lineEDIT_3.text(),
            ffmpeg_path=self.ui.ffmpeg_path_lineEDIT.text(),
            glass_mode=self.ui.theme_pushButton.isChecked(),
            language=self.ui.language_comboBox.currentIndex(),
            theme=self.get_current_theme()
        )
        event.accept()

    def update_presets_list(self):
        self.ui.preset_comboBox.blockSignals(True)
        self.ui.preset_comboBox.clear()
        if self.current_lang == 'Русский':
            self.ui.preset_comboBox.addItem("<Выберите пресет>")
        else:
            self.ui.preset_comboBox.addItem("<Select preset>")
        model = self.ui.preset_comboBox.model()
        item = model.item(0)
        font = item.font()
        font.setBold(True)    
        item.setFont(font)
        self.ui.preset_comboBox.addItems(self.presets.keys())
        self.ui.preset_comboBox.blockSignals(False)

    def save_current_preset(self):
        if self.current_lang == "Русский":
            name, ok = QInputDialog.getText(self, "Сохранить пресет", "Введите имя пресета:")
        else:
            name, ok = QInputDialog.getText(self, "Save preset", "Enter preset name:")
        if not ok or not name.strip():
            return
        name = name.strip()

        if name in '<Выберите пресет>' or name in '<Select preset>':
            if self.current_lang == "Русский":
                QMessageBox.warning(self, "Ошибка", "Недопустимое имя пресета.")
            else:
                QMessageBox.warning(self, "Error", "Invalid preset name.")
            return
        
        preset = {
            "format": self.ui.format_image_comboBox.currentText(),
            "quality": self.ui.image_quality_spinBox.value(),
            "saturation": self.ui.saturation_lineEDIT.text(),
            "contrast": self.ui.contrast_lineEDIT.text(),
            "quality_mode": self.ui.quality_comboBox_image.currentText(),
            "flags": {
                "noice_remover": self.ui.noice_remover_button.isChecked(),
                "better_colours": self.ui.better_colours_button.isChecked(),
                "contrast_sharpness": self.ui.contrast_sharpness_button.isChecked(),
                "better_curcuits": self.ui.better_curcuits_button.isChecked(),
                "dehaze": self.ui.dehaze_button.isChecked(),
                "jpeg_artifacts_remove": self.ui.jpeg_artifacts_remove_button.isChecked(),
                "sepia": self.ui.sepia_button.isChecked()
            }
        }

        self.presets[name] = preset
        save_presets(self.presets)
        self.update_presets_list()
        if self.current_lang == "Русский":
            QMessageBox.information(self, "Готово", f"Пресет '{name}' сохранён.")
        else:
            QMessageBox.information(self, "Done", f"Preset '{name}' saved.")

    def remove_selected_preset(self):
        name = self.ui.preset_comboBox.currentText()
        if name not in self.presets:
            return
        if self.current_lang == "Русский":
            confirm = QMessageBox.question(self, "Удалить пресет", f"Удалить пресет '{name}'?", QMessageBox.Yes | QMessageBox.No)
        else:
            confirm = QMessageBox.question(self, "Delete preset", f"Delete preset '{name}'?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            del self.presets[name]
            save_presets(self.presets)
            self.update_presets_list()
            self.clear_image_effects()

    def clear_image_effects(self):
        self.ui.noice_remover_button.setChecked(False)
        self.ui.better_colours_button.setChecked(False)
        self.ui.contrast_sharpness_button.setChecked(False)
        self.ui.better_curcuits_button.setChecked(False)
        self.ui.dehaze_button.setChecked(False)
        self.ui.jpeg_artifacts_remove_button.setChecked(False)
        self.ui.sepia_button.setChecked(False)
        self.ui.format_image_comboBox.setCurrentIndex(0)
        self.ui.image_quality_spinBox.setValue(95)
        self.ui.saturation_lineEDIT.setText("1.0")
        self.ui.contrast_lineEDIT.setText("1.0")
        self.ui.quality_comboBox_image.setCurrentIndex(0)
        self.ui.image_quality_spinBox.setValue(1)
        self.ui.format_image_comboBox_2.setCurrentIndex(0)
        self.ui.image_quality_spinBox_2.setValue(95)

    def apply_preset(self, name):
        if name in "<Выберите пресет>" or name in "<Choose preset>":
            self.clear_image_effects()
            return
        if name not in self.presets:
            return
        preset = self.presets[name]
        self.ui.format_image_comboBox.setCurrentText(preset["format"])
        self.ui.image_quality_spinBox.setValue(preset["quality"])
        self.ui.saturation_lineEDIT.setText(preset["saturation"])
        self.ui.contrast_lineEDIT.setText(preset["contrast"])
        self.ui.quality_comboBox_image.setCurrentText(preset["quality_mode"])
        flags = preset["flags"]
        self.ui.noice_remover_button.setChecked(flags["noice_remover"])
        self.ui.better_colours_button.setChecked(flags["better_colours"])
        self.ui.contrast_sharpness_button.setChecked(flags["contrast_sharpness"])
        self.ui.better_curcuits_button.setChecked(flags["better_curcuits"])
        self.ui.dehaze_button.setChecked(flags["dehaze"])
        self.ui.jpeg_artifacts_remove_button.setChecked(flags["jpeg_artifacts_remove"])
        self.ui.sepia_button.setChecked(flags["sepia"])

    def choose_output_dir(self):
        if self.current_lang == "Русский":
            folder = QFileDialog.getExistingDirectory(self, "Выберите папку для сохранения")
        else:
            folder = QFileDialog.getExistingDirectory(self, "Select a folder to save")
        if folder:
            self.ui.output_folder.setText(folder)

    def choose_files(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, "Выберите изображения", "",
            "Images (*.png *.jpg *.jpeg *.bmp *.webp *.heic *.heif)"
        )
        if files:
            self.handle_files(files)
    
    def handle_files(self, files):
        exts = (".png", ".jpg", ".jpeg", ".bmp", ".webp", ".heic", ".heif")
        max_preview_side = 100
        for f in files:
            if f in self.loaded_images or not f.lower().endswith(exts):
                continue
            pix = QPixmap()
            ok = pix.load(f)
            if not ok:
                try:
                    with Image.open(f) as im:
                        im.thumbnail((2048, 2048), Image.LANCZOS)
                        if im.mode not in ("RGBA", "RGB"):
                            im = im.convert("RGBA")
                        qimage = ImageQt(im)
                        pix = QPixmap.fromImage(qimage)
                        ok = not pix.isNull()
                except Exception as e:
                    title = "Невозможно открыть файл" if self.current_lang == "Русский" else "Cannot open file"
                    QMessageBox.warning(self, title, f"{os.path.basename(f)}\n{e}")
                    continue
            if not ok or pix.isNull():
                title = "Невозможно открыть файл" if self.current_lang == "Русский" else "Cannot open file"
                QMessageBox.warning(self, title, os.path.basename(f))
                continue
            preview = pix.scaled(max_preview_side, max_preview_side, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            row = QWidget()
            layout = QHBoxLayout(row)
            lbl_img = QLabel(); lbl_img.setPixmap(preview); lbl_img.setFixedSize(max_preview_side, max_preview_side)
            lbl_name = QLabel(os.path.basename(f))
            layout.addWidget(lbl_img); layout.addWidget(lbl_name)
            self.scroll_preview_layout.addWidget(row)
            self.loaded_images.append(f)
            if self.current_lang == "Русский":
                self.ui.added_images_label.setText(f"Добавлено {len(self.loaded_images)} изображений")
            else:
                self.ui.added_images_label.setText(f"Added {len(self.loaded_images)} images")

    def start_processing(self):
        if not self.ui.output_folder.text():
            if self.current_lang == "Русский":
                QMessageBox.warning(self, "Ошибка", "Выберите папку для сохранения.")
            else:
                QMessageBox.warning(self, "Error", "Please select a folder to save.")
            return
        if not torch.cuda.is_available():
            if self.current_lang == "Русский":
                QMessageBox.critical(self, "NVIDIA CUDA не доступна", "Установите её.")
            else:
                QMessageBox.critical(self, "NVIDIA CUDA not found", "Please install it.")
            return
        if not self.loaded_images:
            if self.current_lang == "Русский":
                QMessageBox.warning(self, "Ошибка", "Вы не выбрали изображения.")
            else:
                QMessageBox.warning(self, "Error", "Please select images.")
            return

        fmt_map = {"PNG (default)": "PNG", "JPEG": "JPEG", "WEBP": "WEBP"}
        fmt = fmt_map.get(self.ui.format_image_comboBox.currentText(), "PNG")
        device = torch.device('cuda:0')
        params = {
            'device':       device,
            'model_dir':    self.model_dir,
            'model_name':   None,
            'scale':        None,
            'language':     self.current_lang,
            'do_upscale':   True,
            'output_format': fmt,
            'quality':      self.ui.image_quality_spinBox.value(),
            'output_folder': self.ui.output_folder.text(),
            'saturation':   float(self.ui.saturation_lineEDIT.text() or 1.0),
            'contrast':     float(self.ui.contrast_lineEDIT.text() or 1.0),
            'flags': {
                'noice_remover': self.ui.noice_remover_button.isChecked(),
                'better_colours': self.ui.better_colours_button.isChecked(),
                'contrast_sharpness': self.ui.contrast_sharpness_button.isChecked(),
                'better_curcuits': self.ui.better_curcuits_button.isChecked(),
                'dehaze': self.ui.dehaze_button.isChecked(),
                'jpeg_artifacts_remove': self.ui.jpeg_artifacts_remove_button.isChecked(),
                'sepia': self.ui.sepia_button.isChecked()
            }
        }
        txt = self.ui.quality_comboBox_image.currentText()
        if "No Upscale" in txt:
            params['model_name'], params['scale'], params['do_upscale'] = None, 1, False
        elif "2x" in txt:
            params['model_name'], params['scale'], params['do_upscale'] = 'RealESRGAN_x2plus.pth', 2, True
        elif "4x" in txt and "Anime" in txt:
            params['model_name'], params['scale'], params['do_upscale'] = 'RealESRGAN_x4plus_anime_6B.pth', 4, True
        elif "4x" in txt:
            params['model_name'], params['scale'], params['do_upscale'] = 'RealESRGAN_x4plus.pth', 4, True
        else:
            if self.current_lang == "Русский":
                QMessageBox.critical(self, "Модель не найдена", "Попробуйте другую.")
            else:
                QMessageBox.critical(self, "Model not found", "Please try another one.")
        self.ui.start_processing_button.setEnabled(False)
        self.ui.stop_processing_button.setEnabled(True)
        self.upscale_thread = ImageUpscaleThread(self.loaded_images, params)
        self.upscale_thread.error.connect(self.on_error)
        self.upscale_thread.finished_all.connect(self.on_finished)
        self.upscale_thread.start()
        self.init_cuda_info()

    def start_processing_video(self):
        if not self.loaded_videos:
            if self.current_lang == "Русский":
                QMessageBox.warning(self, "Ошибка", "Вы не выбрали видеофайлы.")
            else:
                QMessageBox.warning(self, "Error", "Please select video files.")
            return
        if not self.ui.output_folder_lineEDIT.text():
            if self.current_lang == "Русский":
                QMessageBox.warning(self, "Ошибка", "Выберите папку для сохранения.")
            else:
                QMessageBox.warning(self, "Error", "Please select a folder to save.")
            return
        if not torch.cuda.is_available():
            if self.current_lang == "Русский":
                QMessageBox.critical(self, "CUDA не обнаружена", "Убедитесь, что установлены драйверы и PyTorch с поддержкой CUDA.")
            else:
                QMessageBox.critical(self, "CUDA not found", "Make sure you have the drivers and PyTorch with CUDA support installed.")
            return

        params = {
            'files': self.loaded_videos,
            'device': torch.device('cuda:0'),
            'model_dir': self.model_dir,
            'model_name': None,
            'scale': None,
            'language': self.current_lang,
            'do_upscale': True,
            'output_format': self.ui.format_image_comboBox_2.currentText().split(" ")[0],
            'codec': self.ui.videocodec_combobox.currentText(),
            'crf': self.ui.crf_quality_spinbox.value(),
            'keep_fps': self.ui.keep_fps_checkbox.isChecked(),
            'remove_audio': self.ui.remove_audio_checkbox.isChecked(),
            'remove_black_lines': self.ui.remove_black_lines_from_upscale_checkbox.isChecked(),
            'remove_metainfo': self.ui.remove_metainfo_from_upscale_checkbox.isChecked(),
            'half_precision': self.ui.half_precision_checkbox_video.isChecked(),
            'ffmpeg_path': self.ui.ffmpeg_path_lineEDIT.text(),
            'output_folder': self.ui.output_folder_lineEDIT.text(),
            'saturation': float(self.ui.saturation_lineEDIT.text() or 1.0),
            'contrast': float(self.ui.contrast_lineEDIT.text() or 1.0),
            'flags': {
                'noice_remover': self.ui.noice_remover_button.isChecked(),
                'better_colours': self.ui.better_colours_button.isChecked(),
                'contrast_sharpness': self.ui.contrast_sharpness_button.isChecked(),
                'better_curcuits': self.ui.better_curcuits_button.isChecked(),
                'dehaze': self.ui.dehaze_button.isChecked(),
                'jpeg_artifacts_remove': self.ui.jpeg_artifacts_remove_button.isChecked(),
                'sepia': self.ui.sepia_button.isChecked(),
            }
        }
        txt = self.ui.quality_comboBox_video.currentText()
        if "No Upscale" in txt:
            params['model_name'], params['scale'], params['do_upscale'] = None, 1, False
        elif "2x" in txt:
            params['model_name'], params['scale'], params['do_upscale'] = 'RealESRGAN_x2plus.pth', 2, True
        elif "3x" in txt and "Anime" in txt:
            params['model_name'], params['scale'], params['do_upscale'] = 'realesr-animevideov3.pth', 3, True
        elif "4x" in txt and "Anime" in txt:
            params['model_name'], params['scale'], params['do_upscale'] = 'RealESRGAN_x4plus_anime_6B.pth', 4, True
        elif "4x" in txt:
            params['model_name'], params['scale'], params['do_upscale'] = 'RealESRGAN_x4plus.pth', 4, True
        else:
            if self.current_lang == "Русский":
                QMessageBox.critical(self, "Модель не найдена", "Попробуйте другую.")
            else:
                QMessageBox.critical(self, "Model not found", "Please try another one.")
            return

        self.ui.start_processing_button.setEnabled(False)
        self.ui.stop_processing_button.setEnabled(True)
        self.video_thread = VideoUpscaleThread(self.loaded_videos, params)
        self.video_thread.update_log.connect(self.ui.log_textEDIT.append)
        self.video_thread.error.connect(self.on_error)
        self.video_thread.finished_all.connect(self.on_finished)
        if self.current_lang == "Русский":
            self.video_thread.file_done.connect(lambda f: self.ui.log_textEDIT.append(f"Обработано: {f}"))
        else:
            self.video_thread.file_done.connect(lambda f: self.ui.log_textEDIT.append(f"Processed: {f}"))
        self.ui.stop_processing_video_button.setEnabled(True)
        self.video_thread.start()
        self.init_cuda_info()

    def stop_processing(self):
        if self.current_lang == "Русский":
            QMessageBox.information(self, "Остановка", "Обработка прервана. Программа будет закрыта.")
        else:
            QMessageBox.information(self, "Stopped", "Processing stopped. The program will close.")
        QApplication.quit()

    def on_error(self, msg):
        if self.current_lang == "Русский":
            QMessageBox.critical(self, "Ошибка", msg)
        else:
            QMessageBox.critical(self, "Error", msg)
        self.ui.start_processing_frames_button.setEnabled(True)
        self.ui.stop_processing_frames_button.setEnabled(False)
        self.ui.start_processing_button.setEnabled(True)
        self.ui.stop_processing_button.setEnabled(False)
        self.init_cuda_info()
        return

    def on_finished(self):
        if hasattr(self, 'frames_thread') and self.frames_thread:
            self.frames_thread.quit()
            self.frames_thread.wait()
            self.frames_thread = None
            self.ui.start_processing_frames_button.setEnabled(True)
            self.ui.stop_processing_frames_button.setEnabled(False)
        if hasattr(self, 'upscale_thread') and self.upscale_thread:
            self.upscale_thread.wait()
            self.upscale_thread = None
        if hasattr(self, 'video_thread') and self.video_thread:
            self.video_thread.wait()
            self.video_thread = None
        if self.current_lang == "Русский":
            QMessageBox.information(self, "Готово", "Все обработано")
        else:
            QMessageBox.information(self, "Done", "All processed")
        self.ui.start_processing_button.setEnabled(True)
        self.ui.stop_processing_button.setEnabled(False)
        self.ui.stop_processing_video_button.setEnabled(False)
        self.init_cuda_info()

    def clear_images(self):
        for i in reversed(range(self.scroll_preview_layout.count())):
            w = self.scroll_preview_layout.itemAt(i).widget()
            if w:
                w.setParent(None)
        self.loaded_images.clear()
        if self.current_lang == 'Русский':
            self.ui.added_images_label.setText("Статус: ожидание")
        else:
            self.ui.added_images_label.setText("Status: waiting")

    def start_ffmpeg_download(self):
        current_lang = self.current_lang
        if current_lang == 'Русский':
            self.ui.log_textEDIT.append("Скачивание FFmpeg...")
        else:
            self.ui.log_textEDIT.append("Downloading FFmpeg...")
        self.ui.ffmpeg_download_button.setEnabled(False)
        self.ui.stop_processing_video_button.setEnabled(True)
        self.ffmpeg_thread = FFmpegDownloadThread()
        self.ffmpeg_thread.finished.connect(self.on_ffmpeg_download_finished)
        self.ffmpeg_thread.error.connect(self.on_ffmpeg_download_error)
        self.ffmpeg_thread.start()

    def on_ffmpeg_download_finished(self, path):
        self.init_cuda_info()
        self.ffmpeg_path = path
        self.ui.ffmpeg_path_lineEDIT.setText(path)
        current_lang = self.current_lang
        if current_lang == 'Русский':
            self.ui.log_textEDIT.append(f"FFmpeg успешно скачан: {path}")
            self.ui.log_textEDIT_3.append(f"FFmpeg успешно скачан: {path}")
        else:
            self.ui.log_textEDIT.append(f"FFmpeg downloaded successfully: {path}")
            self.ui.log_textEDIT_3.append(f"FFmpeg downloaded successfully: {path}")
        self.ui.ffmpeg_download_button.setEnabled(True)
        self.ui.stop_processing_video_button.setEnabled(False)

    def on_ffmpeg_download_error(self, msg):
        current_lang = self.current_lang
        if current_lang == 'Русский':
            self.ui.log_textEDIT.append(f"Ошибка при скачивании FFmpeg: {msg}")
        else:
            self.ui.log_textEDIT.append(f"Error downloading FFmpeg: {msg}")
        self.ui.ffmpeg_download_button.setEnabled(True)

    def choose_videos(self):
        if self.current_lang == 'Русский':
            files, _ = QFileDialog.getOpenFileNames(self, "Выберите видео", "",
            "Videos (*.mp4 *.avi *.mov *.mkv *.webm *.gif)")
        else:
            files, _ = QFileDialog.getOpenFileNames(self, "Choose videos", "",
            "Videos (*.mp4 *.avi *.mov *.mkv *.webm *.gif)")
        if not files:
            return
        for f in files:
            if f not in self.loaded_videos:
                self.loaded_videos.append(f)
        self.ui.input_video_lineEDIT.setText('; '.join(self.loaded_videos))
        if self.current_lang == 'Русский':
            self.ui.status_video_label.setText(f"Добавлено {len(self.loaded_videos)} видео")
        else:
            self.ui.status_video_label.setText(f"Added {len(self.loaded_videos)} videos")

    def choose_video_output_dir(self):
        if self.current_lang == 'Русский':
            folder = QFileDialog.getExistingDirectory(self, "Выберите папку для сохранения видео")
        else:
            folder = QFileDialog.getExistingDirectory(self, "Select a folder to save the video")
        if folder:
            self.ui.output_folder_lineEDIT.setText(folder)

    def choose_ffmpeg_path(self):
        if self.current_lang == 'Русский':
            path, _ = QFileDialog.getOpenFileName(self, "Выберите ffmpeg.exe", "", "Executable (ffmpeg.exe)")
        else:
            path, _ = QFileDialog.getOpenFileName(self, "Choose ffmpeg.exe", "", "Executable (ffmpeg.exe)")
        if path:
            self.ffmpeg_path = path
            self.ui.ffmpeg_path_lineEDIT.setText(path)
            self.ui.ffmpeg_path_lineEDIT_2.setText(path)

    def clear_logs(self):
        self.loaded_videos.clear()
        self.ui.input_video_lineEDIT.clear()
        self.ui.log_textEDIT.clear()
    
    def update_quality_spinbox_state(self):
        fmt = self.ui.format_image_comboBox.currentText()
        if fmt == "PNG (default)":
            self.ui.image_quality_spinBox.setEnabled(False)
        else:
            self.ui.image_quality_spinBox.setEnabled(True)

    def update_quality_spinbox_state_2(self):
        fmt = self.ui.format_image_comboBox_2.currentText()
        if fmt == "PNG (default)":
            self.ui.image_quality_spinBox_2.setEnabled(False)
        else:
            self.ui.image_quality_spinBox_2.setEnabled(True)    

    def choose_videos_to_interpolate(self):
        if self.current_lang == 'Русский':
            files, _ = QFileDialog.getOpenFileNames(self, "Выберите файл для интерполяции", "", "Videos (*.mp4 *.avi *.mov *.mkv *.webm *.gif *.png *.jpg *.jpeg *.bmp *.webp *.heic *.heif)")
        else:
            files, _ = QFileDialog.getOpenFileNames(self, "Select file to interpolate", "", "Videos (*.mp4 *.avi *.mov *.mkv *.gif *.png *.jpg *.jpeg *.bmp *.webp *.heic *.heif)")
        if not files:
            return
        for f in files:
            if f not in self.loaded_interp_videos:
                self.loaded_interp_videos.append(f)
        self.ui.input_video_lineEDIT_3.setText('; '.join(self.loaded_interp_videos))
        if self.current_lang == 'Русский':
            self.ui.status_video_label_3.setText(f"Добавлено {len(self.loaded_interp_videos)} видео")
        else:
            self.ui.status_video_label_3.setText(f"Added {len(self.loaded_interp_videos)} videos")

    def choose_video_to_interpolate_output_dir(self):
        if self.current_lang == 'Русский':
            folder = QFileDialog.getExistingDirectory(self, "Выберите папку для сохранения интерполированного видео")
        else:
            folder = QFileDialog.getExistingDirectory(self, "Select a folder to save the interpolated video")
        if folder:
            self.ui.output_folder_lineEDIT_3.setText(folder)

    def start_frames_processing(self):
        if not self.loaded_interp_videos:
            if self.current_lang == 'Русский':
                QMessageBox.warning(self, "Ошибка", "Вы не выбрали видео для интерполяции.")
            else:
                QMessageBox.warning(self, "Error", "You have not selected any videos for interpolation.")
            return
        output_dir = self.ui.output_folder_lineEDIT_3.text()
        if not output_dir:
            if self.current_lang == 'Русский':
                QMessageBox.warning(self, "Ошибка", "Выберите папку для сохранения.")
            else:
                QMessageBox.warning(self, "Error", "Please select a folder to save the output.")
            return
        txt_factor = self.ui.frames_to_interpolate_comboBox.currentText().strip()
        if not txt_factor:
            if self.current_lang == 'Русский':
                QMessageBox.warning(self, "Ошибка", "Выберите множитель кадров (2x, 3x или 4x).")
            else:
                QMessageBox.warning(self, "Error", "Please select a frame multiplier (2x, 3x, or 4x).")
            return
        m = re.match(r"\s*(\d+)\s*x", txt_factor, re.IGNORECASE)
        if m:
            factor = int(m.group(1))
        else:
            if self.current_lang == 'Русский':
                QMessageBox.warning(self, "Ошибка", f"Невозможно распознать множитель: «{txt_factor}». Будет использовано 1x.")
            else:
                QMessageBox.warning(self, "Error", f"Unable to recognize multiplier: «{txt_factor}». Defaulting to 1x.")
            factor = 1
        params = {
            'files': self.loaded_interp_videos,
            'ffmpeg_path': self.ui.ffmpeg_path_lineEDIT_2.text(),
            'factor': factor,
            'output_folder': output_dir,
            'frame_format': self.ui.format_image_comboBox_4.currentText().split()[0],
            'image_quality': self.ui.image_quality_spinBox_4.value(),
            'codec': self.ui.videocodec_combobox_2.currentText(),
            'crf': self.ui.crf_quality_spinbox_2.value(),
            'language': self.current_lang,
            'remove_black_lines': self.ui.remove_black_lines_checkbox.isChecked(),
            'remove_metainfo': self.ui.remove_metainfo_checkbox.isChecked(),
            'remove_audio': self.ui.remove_audio_checkbox_2.isChecked(),
            'ffmpeg_path': self.ui.ffmpeg_path_lineEDIT_2.text()
        }
        self.ui.start_processing_frames_button.setEnabled(False)
        self.ui.stop_processing_frames_button.setEnabled(True)
        self.frames_thread = FrameGeneratingThread(self.loaded_interp_videos, params)
        self.frames_thread.update_log.connect(self.ui.log_textEDIT_3.append)
        self.frames_thread.error.connect(self.on_error)
        self.frames_thread.finished_all.connect(self.on_finished)
        if self.current_lang == 'Русский':
            self.ui.log_textEDIT_3.append(f"Коэффициент: {factor}")
        else:
            self.ui.log_textEDIT_3.append(f"Coefficient: {factor}")
        self.frames_thread.start()
    
    def clear_frames_logs(self):
        self.ui.log_textEDIT_3.clear()
        self.ui.input_video_lineEDIT_3.clear()
        self.loaded_interp_videos.clear()

    def update_quality_spinbox_state_4(self, fmt: str):
        if fmt.startswith("JPEG") or fmt.startswith("WEBP"):
            self.ui.image_quality_spinBox_4.setEnabled(True)
        else:
            self.ui.image_quality_spinBox_4.setEnabled(False)
        
def main():
    exit_code = 0
    while True:
        try:
            app = QApplication(sys.argv)
        except RuntimeError:
            app = QApplication.instance()
        app.setWindowIcon(QIcon(r"assets/app.png"))
        window = MainWindow()
        window.show()
        exit_code = app.exec()
        if exit_code != EXIT_CODE_REBOOT:
            break
    return exit_code
        
if __name__ == "__main__":
    EXIT_CODE_REBOOT = -11231351
    main()
