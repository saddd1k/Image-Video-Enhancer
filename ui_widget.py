# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSpinBox,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_AI_processer(object):
    def setupUi(self, AI_processer):
        if not AI_processer.objectName():
            AI_processer.setObjectName(u"AI_processer")
        AI_processer.resize(1172, 1032)
        self.main_tab = QTabWidget(AI_processer)
        self.main_tab.setObjectName(u"main_tab")
        self.main_tab.setGeometry(QRect(9, 61, 1161, 961))
        self.image_tab = QWidget()
        self.image_tab.setObjectName(u"image_tab")
        self.choose_images_button = QPushButton(self.image_tab)
        self.choose_images_button.setObjectName(u"choose_images_button")
        self.choose_images_button.setGeometry(QRect(60, 100, 521, 71))
        self.choose_images_button.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: #5365B5;\n"
"    border: 2px dashed #5365B5;\n"
"    border-radius: 5px;\n"
"    padding: 5px 12px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: transparent;\n"
"	color: #8A9AF1;\n"
"	border: 2px dashed #8A9AF1;\n"
"	border-radius: 5px;\n"
"    padding: 5px 12px\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: transparent;\n"
"	color: #566CB8;\n"
"	border: 2px dashed #566CB8;\n"
"	border-radius: 5px;\n"
"    padding: 5px 12px\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.choose_images_button.setFlat(False)
        self.choose_saving_folder_button = QPushButton(self.image_tab)
        self.choose_saving_folder_button.setObjectName(u"choose_saving_folder_button")
        self.choose_saving_folder_button.setGeometry(QRect(60, 180, 521, 61))
        self.choose_saving_folder_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #7187D8;\n"
"    color: white;\n"
"    border: 1px solid #5365B5;\n"
"    border-radius: 5px;\n"
"    padding: 5px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8A9AF1;  \n"
"    border-color: #6B81D8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #566CB8; \n"
"    border-color: #43549D;\n"
"}\n"
"")
        self.output_settings_groupbox = QGroupBox(self.image_tab)
        self.output_settings_groupbox.setObjectName(u"output_settings_groupbox")
        self.output_settings_groupbox.setGeometry(QRect(60, 290, 521, 121))
        self.horizontalLayout = QHBoxLayout(self.output_settings_groupbox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.v_format_label = QVBoxLayout()
        self.v_format_label.setObjectName(u"v_format_label")
        self.output_format_label = QLabel(self.output_settings_groupbox)
        self.output_format_label.setObjectName(u"output_format_label")

        self.v_format_label.addWidget(self.output_format_label)

        self.image_quality_label = QLabel(self.output_settings_groupbox)
        self.image_quality_label.setObjectName(u"image_quality_label")

        self.v_format_label.addWidget(self.image_quality_label)


        self.horizontalLayout.addLayout(self.v_format_label)

        self.v_format_boxes = QVBoxLayout()
        self.v_format_boxes.setObjectName(u"v_format_boxes")
        self.format_image_comboBox = QComboBox(self.output_settings_groupbox)
        self.format_image_comboBox.addItem("")
        self.format_image_comboBox.addItem("")
        self.format_image_comboBox.addItem("")
        self.format_image_comboBox.setObjectName(u"format_image_comboBox")

        self.v_format_boxes.addWidget(self.format_image_comboBox)

        self.image_quality_spinBox = QSpinBox(self.output_settings_groupbox)
        self.image_quality_spinBox.setObjectName(u"image_quality_spinBox")
        self.image_quality_spinBox.setReadOnly(False)
        self.image_quality_spinBox.setMinimum(1)
        self.image_quality_spinBox.setMaximum(100)

        self.v_format_boxes.addWidget(self.image_quality_spinBox)


        self.horizontalLayout.addLayout(self.v_format_boxes)

        self.preset_groupbox = QGroupBox(self.image_tab)
        self.preset_groupbox.setObjectName(u"preset_groupbox")
        self.preset_groupbox.setGeometry(QRect(60, 420, 521, 121))
        self.layoutWidget = QWidget(self.preset_groupbox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 60, 501, 51))
        self.presetbuttons_layout = QHBoxLayout(self.layoutWidget)
        self.presetbuttons_layout.setObjectName(u"presetbuttons_layout")
        self.presetbuttons_layout.setContentsMargins(0, 0, 0, 0)
        self.save_options_button = QPushButton(self.layoutWidget)
        self.save_options_button.setObjectName(u"save_options_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_options_button.sizePolicy().hasHeightForWidth())
        self.save_options_button.setSizePolicy(sizePolicy)
        self.save_options_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #7187D8; \n"
"    color: white;\n"
"    border: 1px solid #5365B5;\n"
"    border-radius: 5px;\n"
"    padding: 5px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8A9AF1; \n"
"    border-color: #6B81D8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #566CB8;  \n"
"    border-color: #43549D;\n"
"}\n"
"")

        self.presetbuttons_layout.addWidget(self.save_options_button)

        self.remove_preset_button = QPushButton(self.layoutWidget)
        self.remove_preset_button.setObjectName(u"remove_preset_button")
        sizePolicy.setHeightForWidth(self.remove_preset_button.sizePolicy().hasHeightForWidth())
        self.remove_preset_button.setSizePolicy(sizePolicy)
        self.remove_preset_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #7187D8; \n"
"    color: white;\n"
"    border: 1px solid #5365B5;\n"
"    border-radius: 5px;\n"
"    padding: 5px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8A9AF1; \n"
"    border-color: #6B81D8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #566CB8;\n"
"    border-color: #43549D;\n"
"}\n"
"")

        self.presetbuttons_layout.addWidget(self.remove_preset_button)

        self.layoutWidget1 = QWidget(self.preset_groupbox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 20, 501, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.load_preset_label = QLabel(self.layoutWidget1)
        self.load_preset_label.setObjectName(u"load_preset_label")

        self.horizontalLayout_2.addWidget(self.load_preset_label)

        self.preset_comboBox = QComboBox(self.layoutWidget1)
        self.preset_comboBox.addItem("")
        self.preset_comboBox.setObjectName(u"preset_comboBox")

        self.horizontalLayout_2.addWidget(self.preset_comboBox)

        self.image_parameters_groupbox = QGroupBox(self.image_tab)
        self.image_parameters_groupbox.setObjectName(u"image_parameters_groupbox")
        self.image_parameters_groupbox.setGeometry(QRect(60, 610, 521, 161))
        self.layoutWidget2 = QWidget(self.image_parameters_groupbox)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(296, 31, 221, 74))
        self.v_image_options_layout_p2 = QVBoxLayout(self.layoutWidget2)
        self.v_image_options_layout_p2.setObjectName(u"v_image_options_layout_p2")
        self.v_image_options_layout_p2.setContentsMargins(0, 0, 0, 0)
        self.jpeg_artifacts_remove_button = QCheckBox(self.layoutWidget2)
        self.jpeg_artifacts_remove_button.setObjectName(u"jpeg_artifacts_remove_button")

        self.v_image_options_layout_p2.addWidget(self.jpeg_artifacts_remove_button)

        self.sepia_button = QCheckBox(self.layoutWidget2)
        self.sepia_button.setObjectName(u"sepia_button")

        self.v_image_options_layout_p2.addWidget(self.sepia_button)

        self.better_curcuits_button = QCheckBox(self.layoutWidget2)
        self.better_curcuits_button.setObjectName(u"better_curcuits_button")

        self.v_image_options_layout_p2.addWidget(self.better_curcuits_button)

        self.layoutWidget3 = QWidget(self.image_parameters_groupbox)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(11, 31, 281, 126))
        self.v_image_options_layout_p1 = QVBoxLayout(self.layoutWidget3)
        self.v_image_options_layout_p1.setObjectName(u"v_image_options_layout_p1")
        self.v_image_options_layout_p1.setContentsMargins(0, 0, 0, 0)
        self.better_faces_button = QCheckBox(self.layoutWidget3)
        self.better_faces_button.setObjectName(u"better_faces_button")

        self.v_image_options_layout_p1.addWidget(self.better_faces_button)

        self.noice_remover_button = QCheckBox(self.layoutWidget3)
        self.noice_remover_button.setObjectName(u"noice_remover_button")

        self.v_image_options_layout_p1.addWidget(self.noice_remover_button)

        self.better_colours_button = QCheckBox(self.layoutWidget3)
        self.better_colours_button.setObjectName(u"better_colours_button")

        self.v_image_options_layout_p1.addWidget(self.better_colours_button)

        self.contrast_sharpness_button = QCheckBox(self.layoutWidget3)
        self.contrast_sharpness_button.setObjectName(u"contrast_sharpness_button")

        self.v_image_options_layout_p1.addWidget(self.contrast_sharpness_button)

        self.dehaze_button = QCheckBox(self.layoutWidget3)
        self.dehaze_button.setObjectName(u"dehaze_button")

        self.v_image_options_layout_p1.addWidget(self.dehaze_button)

        self.added_images_label = QLabel(self.image_tab)
        self.added_images_label.setObjectName(u"added_images_label")
        self.added_images_label.setGeometry(QRect(60, 830, 521, 41))
        self.layoutWidget4 = QWidget(self.image_tab)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(60, 780, 521, 18))
        self.h_filters_with_label_layout = QHBoxLayout(self.layoutWidget4)
        self.h_filters_with_label_layout.setObjectName(u"h_filters_with_label_layout")
        self.h_filters_with_label_layout.setContentsMargins(0, 0, 0, 0)
        self.saturation_image_label = QLabel(self.layoutWidget4)
        self.saturation_image_label.setObjectName(u"saturation_image_label")

        self.h_filters_with_label_layout.addWidget(self.saturation_image_label)

        self.contrast_image_label = QLabel(self.layoutWidget4)
        self.contrast_image_label.setObjectName(u"contrast_image_label")

        self.h_filters_with_label_layout.addWidget(self.contrast_image_label)

        self.layoutWidget5 = QWidget(self.image_tab)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(60, 870, 521, 51))
        self.h_processes_image_layout = QHBoxLayout(self.layoutWidget5)
        self.h_processes_image_layout.setObjectName(u"h_processes_image_layout")
        self.h_processes_image_layout.setContentsMargins(0, 0, 0, 0)
        self.start_processing_button = QPushButton(self.layoutWidget5)
        self.start_processing_button.setObjectName(u"start_processing_button")
        sizePolicy.setHeightForWidth(self.start_processing_button.sizePolicy().hasHeightForWidth())
        self.start_processing_button.setSizePolicy(sizePolicy)
        self.start_processing_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #7187D8;  \n"
"    color: white;\n"
"    border: 1px solid #5365B5;\n"
"    border-radius: 5px;\n"
"    padding: 5px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8A9AF1; \n"
"    border-color: #6B81D8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #566CB8;\n"
"    border-color: #43549D;\n"
"}\n"
"")

        self.h_processes_image_layout.addWidget(self.start_processing_button)

        self.stop_processing_button = QPushButton(self.layoutWidget5)
        self.stop_processing_button.setObjectName(u"stop_processing_button")
        self.stop_processing_button.setEnabled(False)
        sizePolicy.setHeightForWidth(self.stop_processing_button.sizePolicy().hasHeightForWidth())
        self.stop_processing_button.setSizePolicy(sizePolicy)
        self.stop_processing_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #D9534F;\n"
"    color: white;\n"
"    border: 1px solid #B6433F;\n"
"    border-radius: 5px;\n"
"    padding: 5px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #E3827F; \n"
"    border-color: #C96F6A;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #C22E2A;  \n"
"    border-color: #8D211E;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #525252; \n"
"    color: white;          \n"
"    border-color: #525252;    \n"
"}\n"
"")

        self.h_processes_image_layout.addWidget(self.stop_processing_button)

        self.clear_button = QPushButton(self.layoutWidget5)
        self.clear_button.setObjectName(u"clear_button")
        sizePolicy.setHeightForWidth(self.clear_button.sizePolicy().hasHeightForWidth())
        self.clear_button.setSizePolicy(sizePolicy)
        self.clear_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #7187D8;\n"
"    color: white;\n"
"    border: 1px solid #5365B5;\n"
"    border-radius: 5px;\n"
"    padding: 5px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8A9AF1;  \n"
"    border-color: #6B81D8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #566CB8; \n"
"    border-color: #43549D;\n"
"}\n"
"")

        self.h_processes_image_layout.addWidget(self.clear_button)

        self.layoutWidget6 = QWidget(self.image_tab)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(60, 800, 521, 31))
        self.h_lineEDIT_filters_layout = QHBoxLayout(self.layoutWidget6)
        self.h_lineEDIT_filters_layout.setObjectName(u"h_lineEDIT_filters_layout")
        self.h_lineEDIT_filters_layout.setContentsMargins(0, 0, 0, 0)
        self.saturation_lineEDIT = QLineEdit(self.layoutWidget6)
        self.saturation_lineEDIT.setObjectName(u"saturation_lineEDIT")

        self.h_lineEDIT_filters_layout.addWidget(self.saturation_lineEDIT)

        self.contrast_lineEDIT = QLineEdit(self.layoutWidget6)
        self.contrast_lineEDIT.setObjectName(u"contrast_lineEDIT")

        self.h_lineEDIT_filters_layout.addWidget(self.contrast_lineEDIT)

        self.output_folder = QLineEdit(self.image_tab)
        self.output_folder.setObjectName(u"output_folder")
        self.output_folder.setGeometry(QRect(60, 250, 521, 31))
        self.output_folder.setReadOnly(True)
        self.layoutWidget7 = QWidget(self.image_tab)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.layoutWidget7.setGeometry(QRect(600, 60, 541, 861))
        self.scroll_preview_layout = QVBoxLayout(self.layoutWidget7)
        self.scroll_preview_layout.setObjectName(u"scroll_preview_layout")
        self.scroll_preview_layout.setContentsMargins(0, 0, 0, 0)
        self.preview_label = QLabel(self.layoutWidget7)
        self.preview_label.setObjectName(u"preview_label")
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(22)
        self.preview_label.setFont(font)

        self.scroll_preview_layout.addWidget(self.preview_label)

        self.scrollArea = QScrollArea(self.layoutWidget7)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"    border: 2px solid #5365B5;\n"
"    border-radius: 5px;\n"
"    padding: 5px 12px;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_content.setObjectName(u"scroll_content")
        self.scroll_content.setGeometry(QRect(0, 0, 511, 790))
        self.scrollArea.setWidget(self.scroll_content)

        self.scroll_preview_layout.addWidget(self.scrollArea)

        self.layoutWidget8 = QWidget(self.image_tab)
        self.layoutWidget8.setObjectName(u"layoutWidget8")
        self.layoutWidget8.setGeometry(QRect(60, 550, 511, 51))
        self.v_image_scaling_mode_layout = QVBoxLayout(self.layoutWidget8)
        self.v_image_scaling_mode_layout.setObjectName(u"v_image_scaling_mode_layout")
        self.v_image_scaling_mode_layout.setContentsMargins(0, 0, 0, 0)
        self.zoom_mode_label = QLabel(self.layoutWidget8)
        self.zoom_mode_label.setObjectName(u"zoom_mode_label")

        self.v_image_scaling_mode_layout.addWidget(self.zoom_mode_label)

        self.quality_comboBox_image = QComboBox(self.layoutWidget8)
        self.quality_comboBox_image.addItem("")
        self.quality_comboBox_image.addItem("")
        self.quality_comboBox_image.addItem("")
        self.quality_comboBox_image.addItem("")
        self.quality_comboBox_image.setObjectName(u"quality_comboBox_image")

        self.v_image_scaling_mode_layout.addWidget(self.quality_comboBox_image)

        self.main_tab.addTab(self.image_tab, "")
        self.video_tab = QWidget()
        self.video_tab.setObjectName(u"video_tab")
        self.input_output_video_groupBox = QGroupBox(self.video_tab)
        self.input_output_video_groupBox.setObjectName(u"input_output_video_groupBox")
        self.input_output_video_groupBox.setGeometry(QRect(60, 90, 1091, 121))
        self.layoutWidget9 = QWidget(self.input_output_video_groupBox)
        self.layoutWidget9.setObjectName(u"layoutWidget9")
        self.layoutWidget9.setGeometry(QRect(760, 20, 321, 91))
        self.v_input_output_buttons_layout = QVBoxLayout(self.layoutWidget9)
        self.v_input_output_buttons_layout.setObjectName(u"v_input_output_buttons_layout")
        self.v_input_output_buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.input_video_button = QPushButton(self.layoutWidget9)
        self.input_video_button.setObjectName(u"input_video_button")
        self.input_video_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #7187D8;  \n"
"    color: white;\n"
"    border: 1px solid #5365B5;\n"
"    border-radius: 5px;\n"
"    padding: 5px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8A9AF1; \n"
"    border-color: #6B81D8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #566CB8; \n"
"    border-color: #43549D;\n"
"}\n"
"")

        self.v_input_output_buttons_layout.addWidget(self.input_video_button)

        self.output_folder_button = QPushButton(self.layoutWidget9)
        self.output_folder_button.setObjectName(u"output_folder_button")
        self.output_folder_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #7187D8; \n"
"    color: white;\n"
"    border: 1px solid #5365B5;\n"
"    border-radius: 5px;\n"
"    padding: 5px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8A9AF1; \n"
"    border-color: #6B81D8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #566CB8;  \n"
"    border-color: #43549D;\n"
"}\n"
"")

        self.v_input_output_buttons_layout.addWidget(self.output_folder_button)

        self.layoutWidget10 = QWidget(self.input_output_video_groupBox)
        self.layoutWidget10.setObjectName(u"layoutWidget10")
        self.layoutWidget10.setGeometry(QRect(10, 20, 111, 91))
        self.v_input_output_labels_layout = QVBoxLayout(self.layoutWidget10)
        self.v_input_output_labels_layout.setObjectName(u"v_input_output_labels_layout")
        self.v_input_output_labels_layout.setContentsMargins(0, 0, 0, 0)
        self.input_video_label = QLabel(self.layoutWidget10)
        self.input_video_label.setObjectName(u"input_video_label")

        self.v_input_output_labels_layout.addWidget(self.input_video_label)

        self.output_folder_label = QLabel(self.layoutWidget10)
        self.output_folder_label.setObjectName(u"output_folder_label")

        self.v_input_output_labels_layout.addWidget(self.output_folder_label)

        self.layoutWidget11 = QWidget(self.input_output_video_groupBox)
        self.layoutWidget11.setObjectName(u"layoutWidget11")
        self.layoutWidget11.setGeometry(QRect(120, 20, 631, 91))
        self.v_input_output_lineEDIT_layout = QVBoxLayout(self.layoutWidget11)
        self.v_input_output_lineEDIT_layout.setObjectName(u"v_input_output_lineEDIT_layout")
        self.v_input_output_lineEDIT_layout.setContentsMargins(0, 0, 0, 0)
        self.input_video_lineEDIT = QLineEdit(self.layoutWidget11)
        self.input_video_lineEDIT.setObjectName(u"input_video_lineEDIT")
        self.input_video_lineEDIT.setReadOnly(True)

        self.v_input_output_lineEDIT_layout.addWidget(self.input_video_lineEDIT)

        self.output_folder_lineEDIT = QLineEdit(self.layoutWidget11)
        self.output_folder_lineEDIT.setObjectName(u"output_folder_lineEDIT")
        self.output_folder_lineEDIT.setReadOnly(True)

        self.v_input_output_lineEDIT_layout.addWidget(self.output_folder_lineEDIT)

        self.groupBox = QGroupBox(self.video_tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(60, 220, 1091, 271))
        self.layoutWidget12 = QWidget(self.groupBox)
        self.layoutWidget12.setObjectName(u"layoutWidget12")
        self.layoutWidget12.setGeometry(QRect(360, 60, 711, 100))
        self.v_checkboxes_p2_layout = QVBoxLayout(self.layoutWidget12)
        self.v_checkboxes_p2_layout.setObjectName(u"v_checkboxes_p2_layout")
        self.v_checkboxes_p2_layout.setContentsMargins(0, 0, 0, 0)
        self.half_precision_checkbox_video = QCheckBox(self.layoutWidget12)
        self.half_precision_checkbox_video.setObjectName(u"half_precision_checkbox_video")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.half_precision_checkbox_video.sizePolicy().hasHeightForWidth())
        self.half_precision_checkbox_video.setSizePolicy(sizePolicy1)

        self.v_checkboxes_p2_layout.addWidget(self.half_precision_checkbox_video)

        self.dehaze_checkbox_video = QCheckBox(self.layoutWidget12)
        self.dehaze_checkbox_video.setObjectName(u"dehaze_checkbox_video")
        sizePolicy1.setHeightForWidth(self.dehaze_checkbox_video.sizePolicy().hasHeightForWidth())
        self.dehaze_checkbox_video.setSizePolicy(sizePolicy1)

        self.v_checkboxes_p2_layout.addWidget(self.dehaze_checkbox_video)

        self.jpeg_artifacts_checkbox_video = QCheckBox(self.layoutWidget12)
        self.jpeg_artifacts_checkbox_video.setObjectName(u"jpeg_artifacts_checkbox_video")
        sizePolicy1.setHeightForWidth(self.jpeg_artifacts_checkbox_video.sizePolicy().hasHeightForWidth())
        self.jpeg_artifacts_checkbox_video.setSizePolicy(sizePolicy1)

        self.v_checkboxes_p2_layout.addWidget(self.jpeg_artifacts_checkbox_video)

        self.sepia_checkbox_video = QCheckBox(self.layoutWidget12)
        self.sepia_checkbox_video.setObjectName(u"sepia_checkbox_video")
        sizePolicy1.setHeightForWidth(self.sepia_checkbox_video.sizePolicy().hasHeightForWidth())
        self.sepia_checkbox_video.setSizePolicy(sizePolicy1)

        self.v_checkboxes_p2_layout.addWidget(self.sepia_checkbox_video)

        self.layoutWidget13 = QWidget(self.groupBox)
        self.layoutWidget13.setObjectName(u"layoutWidget13")
        self.layoutWidget13.setGeometry(QRect(20, 60, 331, 126))
        self.v_checkboxes_p1_layout = QVBoxLayout(self.layoutWidget13)
        self.v_checkboxes_p1_layout.setObjectName(u"v_checkboxes_p1_layout")
        self.v_checkboxes_p1_layout.setContentsMargins(0, 0, 0, 0)
        self.better_faces_checkbox_video = QCheckBox(self.layoutWidget13)
        self.better_faces_checkbox_video.setObjectName(u"better_faces_checkbox_video")
        sizePolicy1.setHeightForWidth(self.better_faces_checkbox_video.sizePolicy().hasHeightForWidth())
        self.better_faces_checkbox_video.setSizePolicy(sizePolicy1)

        self.v_checkboxes_p1_layout.addWidget(self.better_faces_checkbox_video)

        self.no_noise_checkbox_video = QCheckBox(self.layoutWidget13)
        self.no_noise_checkbox_video.setObjectName(u"no_noise_checkbox_video")
        sizePolicy1.setHeightForWidth(self.no_noise_checkbox_video.sizePolicy().hasHeightForWidth())
        self.no_noise_checkbox_video.setSizePolicy(sizePolicy1)

        self.v_checkboxes_p1_layout.addWidget(self.no_noise_checkbox_video)

        self.better_colors_checkbox_video = QCheckBox(self.layoutWidget13)
        self.better_colors_checkbox_video.setObjectName(u"better_colors_checkbox_video")
        sizePolicy1.setHeightForWidth(self.better_colors_checkbox_video.sizePolicy().hasHeightForWidth())
        self.better_colors_checkbox_video.setSizePolicy(sizePolicy1)

        self.v_checkboxes_p1_layout.addWidget(self.better_colors_checkbox_video)

        self.contrast_sharpness_checkbox_video = QCheckBox(self.layoutWidget13)
        self.contrast_sharpness_checkbox_video.setObjectName(u"contrast_sharpness_checkbox_video")
        sizePolicy1.setHeightForWidth(self.contrast_sharpness_checkbox_video.sizePolicy().hasHeightForWidth())
        self.contrast_sharpness_checkbox_video.setSizePolicy(sizePolicy1)

        self.v_checkboxes_p1_layout.addWidget(self.contrast_sharpness_checkbox_video)

        self.better_circuits_video = QCheckBox(self.layoutWidget13)
        self.better_circuits_video.setObjectName(u"better_circuits_video")
        sizePolicy1.setHeightForWidth(self.better_circuits_video.sizePolicy().hasHeightForWidth())
        self.better_circuits_video.setSizePolicy(sizePolicy1)

        self.v_checkboxes_p1_layout.addWidget(self.better_circuits_video)

        self.layoutWidget14 = QWidget(self.groupBox)
        self.layoutWidget14.setObjectName(u"layoutWidget14")
        self.layoutWidget14.setGeometry(QRect(10, 20, 1071, 26))
        self.h_quality_layout_video = QHBoxLayout(self.layoutWidget14)
        self.h_quality_layout_video.setObjectName(u"h_quality_layout_video")
        self.h_quality_layout_video.setContentsMargins(0, 0, 0, 0)
        self.quality_video_label = QLabel(self.layoutWidget14)
        self.quality_video_label.setObjectName(u"quality_video_label")

        self.h_quality_layout_video.addWidget(self.quality_video_label)

        self.quality_comboBox_video = QComboBox(self.layoutWidget14)
        self.quality_comboBox_video.addItem("")
        self.quality_comboBox_video.addItem("")
        self.quality_comboBox_video.addItem("")
        self.quality_comboBox_video.addItem("")
        self.quality_comboBox_video.addItem("")
        self.quality_comboBox_video.setObjectName(u"quality_comboBox_video")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.quality_comboBox_video.sizePolicy().hasHeightForWidth())
        self.quality_comboBox_video.setSizePolicy(sizePolicy2)

        self.h_quality_layout_video.addWidget(self.quality_comboBox_video)

        self.layoutWidget15 = QWidget(self.groupBox)
        self.layoutWidget15.setObjectName(u"layoutWidget15")
        self.layoutWidget15.setGeometry(QRect(180, 190, 471, 71))
        self.v_contrast_saturation_lineEDIT_layout_video_2 = QVBoxLayout(self.layoutWidget15)
        self.v_contrast_saturation_lineEDIT_layout_video_2.setObjectName(u"v_contrast_saturation_lineEDIT_layout_video_2")
        self.v_contrast_saturation_lineEDIT_layout_video_2.setContentsMargins(0, 0, 0, 0)
        self.saturation_lineEDIT_video = QLineEdit(self.layoutWidget15)
        self.saturation_lineEDIT_video.setObjectName(u"saturation_lineEDIT_video")

        self.v_contrast_saturation_lineEDIT_layout_video_2.addWidget(self.saturation_lineEDIT_video)

        self.contrast_lineEDIT_video = QLineEdit(self.layoutWidget15)
        self.contrast_lineEDIT_video.setObjectName(u"contrast_lineEDIT_video")

        self.v_contrast_saturation_lineEDIT_layout_video_2.addWidget(self.contrast_lineEDIT_video)

        self.layoutWidget16 = QWidget(self.groupBox)
        self.layoutWidget16.setObjectName(u"layoutWidget16")
        self.layoutWidget16.setGeometry(QRect(18, 190, 151, 71))
        self.v_contrast_saturation_label_layout_video = QVBoxLayout(self.layoutWidget16)
        self.v_contrast_saturation_label_layout_video.setObjectName(u"v_contrast_saturation_label_layout_video")
        self.v_contrast_saturation_label_layout_video.setContentsMargins(0, 0, 0, 0)
        self.saturation_label_video = QLabel(self.layoutWidget16)
        self.saturation_label_video.setObjectName(u"saturation_label_video")

        self.v_contrast_saturation_label_layout_video.addWidget(self.saturation_label_video)

        self.contrast_label_video = QLabel(self.layoutWidget16)
        self.contrast_label_video.setObjectName(u"contrast_label_video")

        self.v_contrast_saturation_label_layout_video.addWidget(self.contrast_label_video)

        self.output_and_perfomance_groupbox = QGroupBox(self.video_tab)
        self.output_and_perfomance_groupbox.setObjectName(u"output_and_perfomance_groupbox")
        self.output_and_perfomance_groupbox.setGeometry(QRect(60, 500, 1091, 211))
        self.layoutWidget17 = QWidget(self.output_and_perfomance_groupbox)
        self.layoutWidget17.setObjectName(u"layoutWidget17")
        self.layoutWidget17.setGeometry(QRect(330, 20, 591, 144))
        self.v_perfomance_video_layout = QVBoxLayout(self.layoutWidget17)
        self.v_perfomance_video_layout.setObjectName(u"v_perfomance_video_layout")
        self.v_perfomance_video_layout.setContentsMargins(0, 0, 0, 0)
        self.format_image_comboBox_2 = QComboBox(self.layoutWidget17)
        self.format_image_comboBox_2.addItem("")
        self.format_image_comboBox_2.addItem("")
        self.format_image_comboBox_2.addItem("")
        self.format_image_comboBox_2.setObjectName(u"format_image_comboBox_2")

        self.v_perfomance_video_layout.addWidget(self.format_image_comboBox_2)

        self.image_quality_spinBox_2 = QSpinBox(self.layoutWidget17)
        self.image_quality_spinBox_2.setObjectName(u"image_quality_spinBox_2")
        self.image_quality_spinBox_2.setReadOnly(False)
        self.image_quality_spinBox_2.setMinimum(75)
        self.image_quality_spinBox_2.setMaximum(100)

        self.v_perfomance_video_layout.addWidget(self.image_quality_spinBox_2)

        self.ffmpeg_path_lineEDIT = QLineEdit(self.layoutWidget17)
        self.ffmpeg_path_lineEDIT.setObjectName(u"ffmpeg_path_lineEDIT")
        self.ffmpeg_path_lineEDIT.setReadOnly(True)

        self.v_perfomance_video_layout.addWidget(self.ffmpeg_path_lineEDIT)

        self.videocodec_combobox = QComboBox(self.layoutWidget17)
        self.videocodec_combobox.addItem("")
        self.videocodec_combobox.addItem("")
        self.videocodec_combobox.addItem("")
        self.videocodec_combobox.setObjectName(u"videocodec_combobox")

        self.v_perfomance_video_layout.addWidget(self.videocodec_combobox)

        self.crf_quality_spinbox = QSpinBox(self.layoutWidget17)
        self.crf_quality_spinbox.setObjectName(u"crf_quality_spinbox")
        self.crf_quality_spinbox.setMinimum(0)
        self.crf_quality_spinbox.setMaximum(51)

        self.v_perfomance_video_layout.addWidget(self.crf_quality_spinbox)

        self.layoutWidget18 = QWidget(self.output_and_perfomance_groupbox)
        self.layoutWidget18.setObjectName(u"layoutWidget18")
        self.layoutWidget18.setGeometry(QRect(10, 20, 311, 141))
        self.v_perfomance_labels_layout = QVBoxLayout(self.layoutWidget18)
        self.v_perfomance_labels_layout.setObjectName(u"v_perfomance_labels_layout")
        self.v_perfomance_labels_layout.setContentsMargins(0, 0, 0, 0)
        self.images_format_label_2 = QLabel(self.layoutWidget18)
        self.images_format_label_2.setObjectName(u"images_format_label_2")

        self.v_perfomance_labels_layout.addWidget(self.images_format_label_2)

        self.image_quality_label_2 = QLabel(self.layoutWidget18)
        self.image_quality_label_2.setObjectName(u"image_quality_label_2")

        self.v_perfomance_labels_layout.addWidget(self.image_quality_label_2)

        self.ffmpeg_path_label = QLabel(self.layoutWidget18)
        self.ffmpeg_path_label.setObjectName(u"ffmpeg_path_label")

        self.v_perfomance_labels_layout.addWidget(self.ffmpeg_path_label)

        self.videocodec_label = QLabel(self.layoutWidget18)
        self.videocodec_label.setObjectName(u"videocodec_label")

        self.v_perfomance_labels_layout.addWidget(self.videocodec_label)

        self.quality_crf_label = QLabel(self.layoutWidget18)
        self.quality_crf_label.setObjectName(u"quality_crf_label")
        font1 = QFont()
        font1.setPointSize(8)
        self.quality_crf_label.setFont(font1)

        self.v_perfomance_labels_layout.addWidget(self.quality_crf_label)

        self.layoutWidget19 = QWidget(self.output_and_perfomance_groupbox)
        self.layoutWidget19.setObjectName(u"layoutWidget19")
        self.layoutWidget19.setGeometry(QRect(927, 80, 161, 31))
        self.h_ffmpeg_buttons_layout = QHBoxLayout(self.layoutWidget19)
        self.h_ffmpeg_buttons_layout.setObjectName(u"h_ffmpeg_buttons_layout")
        self.h_ffmpeg_buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.ffmpeg_path_button = QPushButton(self.layoutWidget19)
        self.ffmpeg_path_button.setObjectName(u"ffmpeg_path_button")
        font2 = QFont()
        font2.setPointSize(9)
        self.ffmpeg_path_button.setFont(font2)
        self.ffmpeg_path_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #7187D8;  \n"
"    color: white;\n"
"    border: 1px solid #5365B5;\n"
"    border-radius: 5px;\n"
"    padding: 5px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8A9AF1; \n"
"    border-color: #6B81D8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #566CB8;  \n"
"    border-color: #43549D;\n"
"}\n"
"")

        self.h_ffmpeg_buttons_layout.addWidget(self.ffmpeg_path_button)

        self.ffmpeg_download_button = QPushButton(self.layoutWidget19)
        self.ffmpeg_download_button.setObjectName(u"ffmpeg_download_button")
        self.ffmpeg_download_button.setFont(font2)
        self.ffmpeg_download_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #7187D8;\n"
"    color: white;\n"
"    border: 1px solid #5365B5;\n"
"    border-radius: 5px;\n"
"    padding: 5px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8A9AF1;  \n"
"    border-color: #6B81D8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #566CB8;  \n"
"    border-color: #43549D;\n"
"}\n"
"")

        self.h_ffmpeg_buttons_layout.addWidget(self.ffmpeg_download_button)

        self.layoutWidget20 = QWidget(self.output_and_perfomance_groupbox)
        self.layoutWidget20.setObjectName(u"layoutWidget20")
        self.layoutWidget20.setGeometry(QRect(10, 180, 1071, 22))
        self.h_settings_video_keep_layout = QHBoxLayout(self.layoutWidget20)
        self.h_settings_video_keep_layout.setObjectName(u"h_settings_video_keep_layout")
        self.h_settings_video_keep_layout.setContentsMargins(0, 0, 0, 0)
        self.remove_black_lines_from_upscale_checkbox = QCheckBox(self.layoutWidget20)
        self.remove_black_lines_from_upscale_checkbox.setObjectName(u"remove_black_lines_from_upscale_checkbox")

        self.h_settings_video_keep_layout.addWidget(self.remove_black_lines_from_upscale_checkbox)

        self.remove_metainfo_from_upscale_checkbox = QCheckBox(self.layoutWidget20)
        self.remove_metainfo_from_upscale_checkbox.setObjectName(u"remove_metainfo_from_upscale_checkbox")

        self.h_settings_video_keep_layout.addWidget(self.remove_metainfo_from_upscale_checkbox)

        self.keep_fps_checkbox = QCheckBox(self.layoutWidget20)
        self.keep_fps_checkbox.setObjectName(u"keep_fps_checkbox")
        sizePolicy1.setHeightForWidth(self.keep_fps_checkbox.sizePolicy().hasHeightForWidth())
        self.keep_fps_checkbox.setSizePolicy(sizePolicy1)

        self.h_settings_video_keep_layout.addWidget(self.keep_fps_checkbox)

        self.remove_audio_checkbox = QCheckBox(self.layoutWidget20)
        self.remove_audio_checkbox.setObjectName(u"remove_audio_checkbox")
        sizePolicy1.setHeightForWidth(self.remove_audio_checkbox.sizePolicy().hasHeightForWidth())
        self.remove_audio_checkbox.setSizePolicy(sizePolicy1)

        self.h_settings_video_keep_layout.addWidget(self.remove_audio_checkbox)

        self.status_video_label = QLabel(self.video_tab)
        self.status_video_label.setObjectName(u"status_video_label")
        self.status_video_label.setGeometry(QRect(60, 710, 1091, 31))
        self.log_textEDIT = QTextEdit(self.video_tab)
        self.log_textEDIT.setObjectName(u"log_textEDIT")
        self.log_textEDIT.setGeometry(QRect(60, 740, 1091, 131))
        self.log_textEDIT.setReadOnly(True)
        self.layoutWidget21 = QWidget(self.video_tab)
        self.layoutWidget21.setObjectName(u"layoutWidget21")
        self.layoutWidget21.setGeometry(QRect(60, 880, 1091, 41))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget21)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.start_processing_video_button = QPushButton(self.layoutWidget21)
        self.start_processing_video_button.setObjectName(u"start_processing_video_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.start_processing_video_button.sizePolicy().hasHeightForWidth())
        self.start_processing_video_button.setSizePolicy(sizePolicy3)
        self.start_processing_video_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #7187D8;  \n"
"    color: white;\n"
"    border: 1px solid #5365B5;\n"
"    border-radius: 5px;\n"
"    padding: 5px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8A9AF1; \n"
"    border-color: #6B81D8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #566CB8;\n"
"    border-color: #43549D;\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.start_processing_video_button)

        self.stop_processing_video_button = QPushButton(self.layoutWidget21)
        self.stop_processing_video_button.setObjectName(u"stop_processing_video_button")
        self.stop_processing_video_button.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.stop_processing_video_button.sizePolicy().hasHeightForWidth())
        self.stop_processing_video_button.setSizePolicy(sizePolicy3)
        self.stop_processing_video_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #D9534F;\n"
"    color: white;\n"
"    border: 1px solid #B6433F;\n"
"    border-radius: 5px;\n"
"    padding: 5px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #E3827F; \n"
"    border-color: #C96F6A;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #C22E2A;  \n"
"    border-color: #8D211E;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #525252; \n"
"    color: white;          \n"
"    border-color: #525252;    \n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.stop_processing_video_button)

        self.clear_logs_button = QPushButton(self.layoutWidget21)
        self.clear_logs_button.setObjectName(u"clear_logs_button")
        sizePolicy3.setHeightForWidth(self.clear_logs_button.sizePolicy().hasHeightForWidth())
        self.clear_logs_button.setSizePolicy(sizePolicy3)
        self.clear_logs_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #7187D8;  \n"
"    color: white;\n"
"    border: 1px solid #5365B5;\n"
"    border-radius: 5px;\n"
"    padding: 5px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8A9AF1; \n"
"    border-color: #6B81D8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #566CB8;\n"
"    border-color: #43549D;\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.clear_logs_button)

        self.main_tab.addTab(self.video_tab, "")
        self.generating_frames_tab = QWidget()
        self.generating_frames_tab.setObjectName(u"generating_frames_tab")
        self.input_output_video_groupBox_2 = QGroupBox(self.generating_frames_tab)
        self.input_output_video_groupBox_2.setObjectName(u"input_output_video_groupBox_2")
        self.input_output_video_groupBox_2.setGeometry(QRect(60, 90, 1091, 121))
        self.layoutWidget_8 = QWidget(self.input_output_video_groupBox_2)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(760, 20, 321, 91))
        self.v_input_output_buttons_layout_3 = QVBoxLayout(self.layoutWidget_8)
        self.v_input_output_buttons_layout_3.setObjectName(u"v_input_output_buttons_layout_3")
        self.v_input_output_buttons_layout_3.setContentsMargins(0, 0, 0, 0)
        self.input_video_button_2 = QPushButton(self.layoutWidget_8)
        self.input_video_button_2.setObjectName(u"input_video_button_2")
        self.input_video_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #7187D8;  \n"
"    color: white;\n"
"    border: 1px solid #5365B5;\n"
"    border-radius: 5px;\n"
"    padding: 5px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8A9AF1; \n"
"    border-color: #6B81D8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #566CB8; \n"
"    border-color: #43549D;\n"
"}\n"
"")

        self.v_input_output_buttons_layout_3.addWidget(self.input_video_button_2)

        self.output_folder_button_2 = QPushButton(self.layoutWidget_8)
        self.output_folder_button_2.setObjectName(u"output_folder_button_2")
        self.output_folder_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #7187D8; \n"
"    color: white;\n"
"    border: 1px solid #5365B5;\n"
"    border-radius: 5px;\n"
"    padding: 5px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8A9AF1; \n"
"    border-color: #6B81D8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #566CB8;  \n"
"    border-color: #43549D;\n"
"}\n"
"")

        self.v_input_output_buttons_layout_3.addWidget(self.output_folder_button_2)

        self.layoutWidget_9 = QWidget(self.input_output_video_groupBox_2)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(10, 20, 111, 91))
        self.v_input_output_labels_layout_3 = QVBoxLayout(self.layoutWidget_9)
        self.v_input_output_labels_layout_3.setObjectName(u"v_input_output_labels_layout_3")
        self.v_input_output_labels_layout_3.setContentsMargins(0, 0, 0, 0)
        self.input_video_label_3 = QLabel(self.layoutWidget_9)
        self.input_video_label_3.setObjectName(u"input_video_label_3")

        self.v_input_output_labels_layout_3.addWidget(self.input_video_label_3)

        self.output_folder_label_3 = QLabel(self.layoutWidget_9)
        self.output_folder_label_3.setObjectName(u"output_folder_label_3")

        self.v_input_output_labels_layout_3.addWidget(self.output_folder_label_3)

        self.layoutWidget_10 = QWidget(self.input_output_video_groupBox_2)
        self.layoutWidget_10.setObjectName(u"layoutWidget_10")
        self.layoutWidget_10.setGeometry(QRect(120, 20, 631, 91))
        self.v_input_output_lineEDIT_layout_3 = QVBoxLayout(self.layoutWidget_10)
        self.v_input_output_lineEDIT_layout_3.setObjectName(u"v_input_output_lineEDIT_layout_3")
        self.v_input_output_lineEDIT_layout_3.setContentsMargins(0, 0, 0, 0)
        self.input_video_lineEDIT_3 = QLineEdit(self.layoutWidget_10)
        self.input_video_lineEDIT_3.setObjectName(u"input_video_lineEDIT_3")
        self.input_video_lineEDIT_3.setReadOnly(True)

        self.v_input_output_lineEDIT_layout_3.addWidget(self.input_video_lineEDIT_3)

        self.output_folder_lineEDIT_3 = QLineEdit(self.layoutWidget_10)
        self.output_folder_lineEDIT_3.setObjectName(u"output_folder_lineEDIT_3")
        self.output_folder_lineEDIT_3.setReadOnly(True)

        self.v_input_output_lineEDIT_layout_3.addWidget(self.output_folder_lineEDIT_3)

        self.log_textEDIT_3 = QTextEdit(self.generating_frames_tab)
        self.log_textEDIT_3.setObjectName(u"log_textEDIT_3")
        self.log_textEDIT_3.setGeometry(QRect(60, 570, 1091, 301))
        self.log_textEDIT_3.setReadOnly(True)
        self.status_video_label_3 = QLabel(self.generating_frames_tab)
        self.status_video_label_3.setObjectName(u"status_video_label_3")
        self.status_video_label_3.setGeometry(QRect(60, 520, 1081, 51))
        self.layoutWidget22 = QWidget(self.generating_frames_tab)
        self.layoutWidget22.setObjectName(u"layoutWidget22")
        self.layoutWidget22.setGeometry(QRect(60, 220, 1081, 71))
        self.h_fps_layout = QHBoxLayout(self.layoutWidget22)
        self.h_fps_layout.setObjectName(u"h_fps_layout")
        self.h_fps_layout.setContentsMargins(0, 0, 0, 0)
        self.frames_to_interpolate_label = QLabel(self.layoutWidget22)
        self.frames_to_interpolate_label.setObjectName(u"frames_to_interpolate_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frames_to_interpolate_label.sizePolicy().hasHeightForWidth())
        self.frames_to_interpolate_label.setSizePolicy(sizePolicy4)

        self.h_fps_layout.addWidget(self.frames_to_interpolate_label)

        self.frames_to_interpolate_comboBox = QComboBox(self.layoutWidget22)
        self.frames_to_interpolate_comboBox.addItem("")
        self.frames_to_interpolate_comboBox.addItem("")
        self.frames_to_interpolate_comboBox.addItem("")
        self.frames_to_interpolate_comboBox.addItem("")
        self.frames_to_interpolate_comboBox.setObjectName(u"frames_to_interpolate_comboBox")
        sizePolicy2.setHeightForWidth(self.frames_to_interpolate_comboBox.sizePolicy().hasHeightForWidth())
        self.frames_to_interpolate_comboBox.setSizePolicy(sizePolicy2)

        self.h_fps_layout.addWidget(self.frames_to_interpolate_comboBox)

        self.output_and_perfomance_groupbox_2 = QGroupBox(self.generating_frames_tab)
        self.output_and_perfomance_groupbox_2.setObjectName(u"output_and_perfomance_groupbox_2")
        self.output_and_perfomance_groupbox_2.setGeometry(QRect(60, 300, 1091, 221))
        self.layoutWidget_3 = QWidget(self.output_and_perfomance_groupbox_2)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(330, 20, 591, 144))
        self.v_perfomance_video_layout_2 = QVBoxLayout(self.layoutWidget_3)
        self.v_perfomance_video_layout_2.setObjectName(u"v_perfomance_video_layout_2")
        self.v_perfomance_video_layout_2.setContentsMargins(0, 0, 0, 0)
        self.format_image_comboBox_4 = QComboBox(self.layoutWidget_3)
        self.format_image_comboBox_4.addItem("")
        self.format_image_comboBox_4.addItem("")
        self.format_image_comboBox_4.addItem("")
        self.format_image_comboBox_4.setObjectName(u"format_image_comboBox_4")

        self.v_perfomance_video_layout_2.addWidget(self.format_image_comboBox_4)

        self.image_quality_spinBox_4 = QSpinBox(self.layoutWidget_3)
        self.image_quality_spinBox_4.setObjectName(u"image_quality_spinBox_4")
        self.image_quality_spinBox_4.setReadOnly(False)
        self.image_quality_spinBox_4.setMinimum(75)
        self.image_quality_spinBox_4.setMaximum(100)

        self.v_perfomance_video_layout_2.addWidget(self.image_quality_spinBox_4)

        self.ffmpeg_path_lineEDIT_2 = QLineEdit(self.layoutWidget_3)
        self.ffmpeg_path_lineEDIT_2.setObjectName(u"ffmpeg_path_lineEDIT_2")
        self.ffmpeg_path_lineEDIT_2.setReadOnly(True)

        self.v_perfomance_video_layout_2.addWidget(self.ffmpeg_path_lineEDIT_2)

        self.videocodec_combobox_2 = QComboBox(self.layoutWidget_3)
        self.videocodec_combobox_2.addItem("")
        self.videocodec_combobox_2.addItem("")
        self.videocodec_combobox_2.addItem("")
        self.videocodec_combobox_2.setObjectName(u"videocodec_combobox_2")

        self.v_perfomance_video_layout_2.addWidget(self.videocodec_combobox_2)

        self.crf_quality_spinbox_2 = QSpinBox(self.layoutWidget_3)
        self.crf_quality_spinbox_2.setObjectName(u"crf_quality_spinbox_2")
        self.crf_quality_spinbox_2.setMinimum(0)
        self.crf_quality_spinbox_2.setMaximum(51)

        self.v_perfomance_video_layout_2.addWidget(self.crf_quality_spinbox_2)

        self.layoutWidget_5 = QWidget(self.output_and_perfomance_groupbox_2)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(10, 20, 311, 141))
        self.v_perfomance_labels_layout_2 = QVBoxLayout(self.layoutWidget_5)
        self.v_perfomance_labels_layout_2.setObjectName(u"v_perfomance_labels_layout_2")
        self.v_perfomance_labels_layout_2.setContentsMargins(0, 0, 0, 0)
        self.images_format_label_3 = QLabel(self.layoutWidget_5)
        self.images_format_label_3.setObjectName(u"images_format_label_3")

        self.v_perfomance_labels_layout_2.addWidget(self.images_format_label_3)

        self.image_quality_label_4 = QLabel(self.layoutWidget_5)
        self.image_quality_label_4.setObjectName(u"image_quality_label_4")

        self.v_perfomance_labels_layout_2.addWidget(self.image_quality_label_4)

        self.ffmpeg_path_label_2 = QLabel(self.layoutWidget_5)
        self.ffmpeg_path_label_2.setObjectName(u"ffmpeg_path_label_2")

        self.v_perfomance_labels_layout_2.addWidget(self.ffmpeg_path_label_2)

        self.videocodec_label_2 = QLabel(self.layoutWidget_5)
        self.videocodec_label_2.setObjectName(u"videocodec_label_2")

        self.v_perfomance_labels_layout_2.addWidget(self.videocodec_label_2)

        self.quality_crf_label_2 = QLabel(self.layoutWidget_5)
        self.quality_crf_label_2.setObjectName(u"quality_crf_label_2")
        self.quality_crf_label_2.setFont(font1)

        self.v_perfomance_labels_layout_2.addWidget(self.quality_crf_label_2)

        self.layoutWidget_6 = QWidget(self.output_and_perfomance_groupbox_2)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(927, 80, 161, 31))
        self.h_ffmpeg_buttons_layout_2 = QHBoxLayout(self.layoutWidget_6)
        self.h_ffmpeg_buttons_layout_2.setObjectName(u"h_ffmpeg_buttons_layout_2")
        self.h_ffmpeg_buttons_layout_2.setContentsMargins(0, 0, 0, 0)
        self.ffmpeg_path_button_2 = QPushButton(self.layoutWidget_6)
        self.ffmpeg_path_button_2.setObjectName(u"ffmpeg_path_button_2")
        self.ffmpeg_path_button_2.setFont(font2)
        self.ffmpeg_path_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #7187D8;  \n"
"    color: white;\n"
"    border: 1px solid #5365B5;\n"
"    border-radius: 5px;\n"
"    padding: 5px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8A9AF1; \n"
"    border-color: #6B81D8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #566CB8;  \n"
"    border-color: #43549D;\n"
"}\n"
"")

        self.h_ffmpeg_buttons_layout_2.addWidget(self.ffmpeg_path_button_2)

        self.ffmpeg_download_button_2 = QPushButton(self.layoutWidget_6)
        self.ffmpeg_download_button_2.setObjectName(u"ffmpeg_download_button_2")
        self.ffmpeg_download_button_2.setFont(font2)
        self.ffmpeg_download_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #7187D8;\n"
"    color: white;\n"
"    border: 1px solid #5365B5;\n"
"    border-radius: 5px;\n"
"    padding: 5px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8A9AF1;  \n"
"    border-color: #6B81D8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #566CB8;  \n"
"    border-color: #43549D;\n"
"}\n"
"")

        self.h_ffmpeg_buttons_layout_2.addWidget(self.ffmpeg_download_button_2)

        self.layoutWidget_7 = QWidget(self.output_and_perfomance_groupbox_2)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(10, 180, 1071, 22))
        self.h_settings_video_keep_layout_2 = QHBoxLayout(self.layoutWidget_7)
        self.h_settings_video_keep_layout_2.setObjectName(u"h_settings_video_keep_layout_2")
        self.h_settings_video_keep_layout_2.setContentsMargins(0, 0, 0, 0)
        self.remove_black_lines_checkbox = QCheckBox(self.layoutWidget_7)
        self.remove_black_lines_checkbox.setObjectName(u"remove_black_lines_checkbox")

        self.h_settings_video_keep_layout_2.addWidget(self.remove_black_lines_checkbox)

        self.remove_metainfo_checkbox = QCheckBox(self.layoutWidget_7)
        self.remove_metainfo_checkbox.setObjectName(u"remove_metainfo_checkbox")

        self.h_settings_video_keep_layout_2.addWidget(self.remove_metainfo_checkbox)

        self.remove_audio_checkbox_2 = QCheckBox(self.layoutWidget_7)
        self.remove_audio_checkbox_2.setObjectName(u"remove_audio_checkbox_2")
        sizePolicy1.setHeightForWidth(self.remove_audio_checkbox_2.sizePolicy().hasHeightForWidth())
        self.remove_audio_checkbox_2.setSizePolicy(sizePolicy1)

        self.h_settings_video_keep_layout_2.addWidget(self.remove_audio_checkbox_2)

        self.layoutWidget23 = QWidget(self.generating_frames_tab)
        self.layoutWidget23.setObjectName(u"layoutWidget23")
        self.layoutWidget23.setGeometry(QRect(60, 880, 1091, 41))
        self.h_processing_butons_frames_layout = QHBoxLayout(self.layoutWidget23)
        self.h_processing_butons_frames_layout.setObjectName(u"h_processing_butons_frames_layout")
        self.h_processing_butons_frames_layout.setContentsMargins(0, 0, 0, 0)
        self.start_processing_frames_button = QPushButton(self.layoutWidget23)
        self.start_processing_frames_button.setObjectName(u"start_processing_frames_button")
        sizePolicy3.setHeightForWidth(self.start_processing_frames_button.sizePolicy().hasHeightForWidth())
        self.start_processing_frames_button.setSizePolicy(sizePolicy3)
        self.start_processing_frames_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #7187D8;  \n"
"    color: white;\n"
"    border: 1px solid #5365B5;\n"
"    border-radius: 5px;\n"
"    padding: 5px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8A9AF1; \n"
"    border-color: #6B81D8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #566CB8; \n"
"    border-color: #43549D;\n"
"}\n"
"")

        self.h_processing_butons_frames_layout.addWidget(self.start_processing_frames_button)

        self.stop_processing_frames_button = QPushButton(self.layoutWidget23)
        self.stop_processing_frames_button.setObjectName(u"stop_processing_frames_button")
        self.stop_processing_frames_button.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.stop_processing_frames_button.sizePolicy().hasHeightForWidth())
        self.stop_processing_frames_button.setSizePolicy(sizePolicy3)
        self.stop_processing_frames_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #D9534F;\n"
"    color: white;\n"
"    border: 1px solid #B6433F;\n"
"    border-radius: 5px;\n"
"    padding: 5px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #E3827F; \n"
"    border-color: #C96F6A;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #C22E2A;  \n"
"    border-color: #8D211E;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #525252; \n"
"    color: white;          \n"
"    border-color: #525252;    \n"
"}\n"
"")

        self.h_processing_butons_frames_layout.addWidget(self.stop_processing_frames_button)

        self.clear_frame_output_button = QPushButton(self.layoutWidget23)
        self.clear_frame_output_button.setObjectName(u"clear_frame_output_button")
        sizePolicy3.setHeightForWidth(self.clear_frame_output_button.sizePolicy().hasHeightForWidth())
        self.clear_frame_output_button.setSizePolicy(sizePolicy3)
        self.clear_frame_output_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #7187D8;  \n"
"    color: white;\n"
"    border: 1px solid #5365B5;\n"
"    border-radius: 5px;\n"
"    padding: 5px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8A9AF1; \n"
"    border-color: #6B81D8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #566CB8; \n"
"    border-color: #43549D;\n"
"}\n"
"")

        self.h_processing_butons_frames_layout.addWidget(self.clear_frame_output_button)

        self.main_tab.addTab(self.generating_frames_tab, "")
        self.program_info_tab = QWidget()
        self.program_info_tab.setObjectName(u"program_info_tab")
        self.cuda_info_groopbox = QGroupBox(self.program_info_tab)
        self.cuda_info_groopbox.setObjectName(u"cuda_info_groopbox")
        self.cuda_info_groopbox.setGeometry(QRect(60, 90, 1081, 281))
        self.cuda_info_widget = QWidget(self.cuda_info_groopbox)
        self.cuda_info_widget.setObjectName(u"cuda_info_widget")
        self.cuda_info_widget.setGeometry(QRect(10, 110, 1061, 111))
        self.cuda_info_widget.setStyleSheet(u"")
        self.cuda_devices_label = QLabel(self.cuda_info_widget)
        self.cuda_devices_label.setObjectName(u"cuda_devices_label")
        self.cuda_devices_label.setGeometry(QRect(-10, 0, 211, 31))
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.cuda_devices_label.sizePolicy().hasHeightForWidth())
        self.cuda_devices_label.setSizePolicy(sizePolicy5)
        self.cuda_devices_label.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"}")
        self.cuda_mode = QLabel(self.cuda_info_groopbox)
        self.cuda_mode.setObjectName(u"cuda_mode")
        self.cuda_mode.setGeometry(QRect(10, 230, 121, 20))
        self.gp_cuda_info_label = QLabel(self.cuda_info_groopbox)
        self.gp_cuda_info_label.setObjectName(u"gp_cuda_info_label")
        self.gp_cuda_info_label.setGeometry(QRect(10, 250, 761, 21))
        self.layoutWidget24 = QWidget(self.cuda_info_groopbox)
        self.layoutWidget24.setObjectName(u"layoutWidget24")
        self.layoutWidget24.setGeometry(QRect(10, 30, 1061, 62))
        self.v_cuda_info_layout = QVBoxLayout(self.layoutWidget24)
        self.v_cuda_info_layout.setObjectName(u"v_cuda_info_layout")
        self.v_cuda_info_layout.setContentsMargins(0, 0, 0, 0)
        self.cuda_accessibility_label = QLabel(self.layoutWidget24)
        self.cuda_accessibility_label.setObjectName(u"cuda_accessibility_label")

        self.v_cuda_info_layout.addWidget(self.cuda_accessibility_label)

        self.cuda_status_label = QLabel(self.layoutWidget24)
        self.cuda_status_label.setObjectName(u"cuda_status_label")

        self.v_cuda_info_layout.addWidget(self.cuda_status_label)

        self.cuda_information_label = QLabel(self.layoutWidget24)
        self.cuda_information_label.setObjectName(u"cuda_information_label")

        self.v_cuda_info_layout.addWidget(self.cuda_information_label)

        self.cuda_update_pushButton = QPushButton(self.cuda_info_groopbox)
        self.cuda_update_pushButton.setObjectName(u"cuda_update_pushButton")
        self.cuda_update_pushButton.setGeometry(QRect(1000, 250, 75, 24))
        self.interpolation_info_groupbox = QGroupBox(self.program_info_tab)
        self.interpolation_info_groupbox.setObjectName(u"interpolation_info_groupbox")
        self.interpolation_info_groupbox.setGeometry(QRect(60, 380, 1081, 541))
        self.interpolation_info_label = QLabel(self.interpolation_info_groupbox)
        self.interpolation_info_label.setObjectName(u"interpolation_info_label")
        self.interpolation_info_label.setGeometry(QRect(10, 30, 1051, 191))
        self.layoutWidget25 = QWidget(self.interpolation_info_groupbox)
        self.layoutWidget25.setObjectName(u"layoutWidget25")
        self.layoutWidget25.setGeometry(QRect(8, 229, 1061, 301))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget25)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gifLabelI2 = QLabel(self.layoutWidget25)
        self.gifLabelI2.setObjectName(u"gifLabelI2")

        self.horizontalLayout_5.addWidget(self.gifLabelI2)

        self.gifLabelD2 = QLabel(self.layoutWidget25)
        self.gifLabelD2.setObjectName(u"gifLabelD2")

        self.horizontalLayout_5.addWidget(self.gifLabelD2)

        self.main_tab.addTab(self.program_info_tab, "")
        self.language_label = QLabel(AI_processer)
        self.language_label.setObjectName(u"language_label")
        self.language_label.setGeometry(QRect(8, 9, 71, 31))
        self.language_comboBox = QComboBox(AI_processer)
        self.language_comboBox.addItem("")
        self.language_comboBox.addItem("")
        self.language_comboBox.setObjectName(u"language_comboBox")
        self.language_comboBox.setGeometry(QRect(80, 10, 151, 31))
        sizePolicy3.setHeightForWidth(self.language_comboBox.sizePolicy().hasHeightForWidth())
        self.language_comboBox.setSizePolicy(sizePolicy3)
        self.model_status_label = QLabel(AI_processer)
        self.model_status_label.setObjectName(u"model_status_label")
        self.model_status_label.setGeometry(QRect(961, 11, 211, 31))
        self.model_status_badge_label = QLabel(AI_processer)
        self.model_status_badge_label.setObjectName(u"model_status_badge_label")
        self.model_status_badge_label.setGeometry(QRect(902, 11, 51, 32))
        self.model_status_badge_label.setStyleSheet(u"")
        self.layoutWidget26 = QWidget(AI_processer)
        self.layoutWidget26.setObjectName(u"layoutWidget26")
        self.layoutWidget26.setGeometry(QRect(810, 50, 361, 31))
        self.h_themes_layout = QHBoxLayout(self.layoutWidget26)
        self.h_themes_layout.setObjectName(u"h_themes_layout")
        self.h_themes_layout.setContentsMargins(0, 0, 0, 0)
        self.dark_theme_radio = QRadioButton(self.layoutWidget26)
        self.dark_theme_radio.setObjectName(u"dark_theme_radio")
        self.dark_theme_radio.setStyleSheet(u"QRadioButton::indicator {\n"
"        width: 15px;\n"
"        height: 15px;\n"
"        border-radius: 7px;\n"
"        border: 2px solid gray;\n"
"    }\n"
"    QRadioButton::indicator:checked {\n"
"        background-color: #4444cc;\n"
"        border: 2px solid #222299;\n"
"    }")
        self.dark_theme_radio.setChecked(True)

        self.h_themes_layout.addWidget(self.dark_theme_radio)

        self.light_theme_radio = QRadioButton(self.layoutWidget26)
        self.light_theme_radio.setObjectName(u"light_theme_radio")
        self.light_theme_radio.setStyleSheet(u"QRadioButton::indicator {\n"
"        width: 15px;\n"
"        height: 15px;\n"
"        border-radius: 7px;\n"
"        border: 2px solid gray;\n"
"    }\n"
"    QRadioButton::indicator:checked {\n"
"        background-color: #edf1ff;\n"
"        border: 2px solid #ffffff;\n"
"    }")
        self.light_theme_radio.setChecked(False)

        self.h_themes_layout.addWidget(self.light_theme_radio)

        self.castle_theme_radio = QRadioButton(self.layoutWidget26)
        self.castle_theme_radio.setObjectName(u"castle_theme_radio")
        self.castle_theme_radio.setStyleSheet(u"QRadioButton::indicator {\n"
"        width: 15px;\n"
"        height: 15px;\n"
"        border-radius: 7px;\n"
"        border: 2px solid gray;\n"
"    }\n"
"    QRadioButton::indicator:checked {\n"
"        background-color: #FFA500;  /* \u043c\u043e\u0440\u043a\u043e\u0432\u043d\u043e-\u043e\u0440\u0430\u043d\u0436\u0435\u0432\u044b\u0439 */\n"
"        border: 2px solid #cc7000;\n"
"    }")

        self.h_themes_layout.addWidget(self.castle_theme_radio)

        self.theme_pushButton = QPushButton(self.layoutWidget26)
        self.theme_pushButton.setObjectName(u"theme_pushButton")
        sizePolicy1.setHeightForWidth(self.theme_pushButton.sizePolicy().hasHeightForWidth())
        self.theme_pushButton.setSizePolicy(sizePolicy1)
        self.theme_pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #7187D8;\n"
"    color: white;\n"
"    border: 1px solid #5365B5;\n"
"    border-radius: 5px;\n"
"    padding: 5px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8A9AF1;  \n"
"    border-color: #6B81D8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #566CB8; \n"
"    border-color: #43549D;\n"
"}\n"
"")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.UserAvailable))
        self.theme_pushButton.setIcon(icon)
        self.theme_pushButton.setCheckable(True)

        self.h_themes_layout.addWidget(self.theme_pushButton)


        self.retranslateUi(AI_processer)

        self.main_tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AI_processer)
    # setupUi

    def retranslateUi(self, AI_processer):
        AI_processer.setWindowTitle(QCoreApplication.translate("AI_processer", u"Artificial intelligence processer", None))
        self.choose_images_button.setText(QCoreApplication.translate("AI_processer", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
        self.choose_saving_folder_button.setText(QCoreApplication.translate("AI_processer", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0430\u043f\u043a\u0443 \u0434\u043b\u044f \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f", None))
        self.output_settings_groupbox.setTitle(QCoreApplication.translate("AI_processer", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0432\u044b\u0432\u043e\u0434\u0430", None))
        self.output_format_label.setText(QCoreApplication.translate("AI_processer", u"\u0424\u043e\u0440\u043c\u0430\u0442 \u0432\u044b\u0432\u043e\u0434\u0430:", None))
        self.image_quality_label.setText(QCoreApplication.translate("AI_processer", u"\u041a\u0430\u0447\u0435\u0441\u0442\u0432\u043e (\u0434\u043b\u044f JPEG/WEBP, 1-100):", None))
        self.format_image_comboBox.setItemText(0, QCoreApplication.translate("AI_processer", u"PNG (default)", None))
        self.format_image_comboBox.setItemText(1, QCoreApplication.translate("AI_processer", u"JPEG", None))
        self.format_image_comboBox.setItemText(2, QCoreApplication.translate("AI_processer", u"WEBP", None))

        self.preset_groupbox.setTitle(QCoreApplication.translate("AI_processer", u"\u041f\u0440\u0435\u0441\u0435\u0442\u044b", None))
        self.save_options_button.setText(QCoreApplication.translate("AI_processer", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0442\u0435\u043a\u0443\u0449\u0438\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.remove_preset_button.setText(QCoreApplication.translate("AI_processer", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u043f\u0440\u0435\u0441\u0435\u0442", None))
        self.load_preset_label.setText(QCoreApplication.translate("AI_processer", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043f\u0435\u0440\u0435\u0441\u0435\u0442:", None))
        self.preset_comboBox.setItemText(0, QCoreApplication.translate("AI_processer", u"<\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0440\u0435\u0441\u0435\u0442>", None))

        self.image_parameters_groupbox.setTitle(QCoreApplication.translate("AI_processer", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438", None))
        self.jpeg_artifacts_remove_button.setText(QCoreApplication.translate("AI_processer", u"\u0423\u0441\u0442\u0440\u0430\u043d\u0438\u0442\u044c JPEG-\u0430\u0440\u0442\u0435\u0444\u0430\u043a\u0442\u044b", None))
        self.sepia_button.setText(QCoreApplication.translate("AI_processer", u"\u0421\u0442\u0438\u043b\u0438\u0437\u0430\u0446\u0438\u044f (\u0441\u0435\u043f\u0438\u044f)", None))
        self.better_curcuits_button.setText(QCoreApplication.translate("AI_processer", u"\u0423\u0441\u0438\u043b\u0435\u043d\u0438\u0435 \u043a\u043e\u043d\u0442\u0443\u0440\u043e\u0432", None))
        self.better_faces_button.setText(QCoreApplication.translate("AI_processer", u"\u0423\u043b\u0443\u0447\u0448\u0438\u0442\u044c \u043b\u0438\u0446\u0430", None))
        self.noice_remover_button.setText(QCoreApplication.translate("AI_processer", u"\u041f\u0440\u0435\u0434\u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 (\u0448\u0443\u043c)", None))
        self.better_colours_button.setText(QCoreApplication.translate("AI_processer", u"\u0423\u043b\u0443\u0447\u0448\u0435\u043d\u0438\u0435 \u0446\u0432\u0435\u0442\u0430", None))
        self.contrast_sharpness_button.setText(QCoreApplication.translate("AI_processer", u"\u041f\u043e\u0441\u0442\u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 (\u0440\u0435\u0437\u043a\u043e\u0441\u0442\u044c/\u043a\u043e\u043d\u0442\u0440\u0430\u0441\u0442)", None))
        self.dehaze_button.setText(QCoreApplication.translate("AI_processer", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0442\u0443\u043c\u0430\u043d (dehaze)", None))
        self.added_images_label.setText(QCoreApplication.translate("AI_processer", u"\u0421\u0442\u0430\u0442\u0443\u0441: \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u0435", None))
        self.saturation_image_label.setText(QCoreApplication.translate("AI_processer", u"\u041d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u043e\u0441\u0442\u044c:", None))
        self.contrast_image_label.setText(QCoreApplication.translate("AI_processer", u"\u041a\u043e\u043d\u0442\u0440\u0430\u0441\u0442:", None))
        self.start_processing_button.setText(QCoreApplication.translate("AI_processer", u"\u041d\u0430\u0447\u0430\u0442\u044c \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0443", None))
        self.stop_processing_button.setText(QCoreApplication.translate("AI_processer", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0438 \u0432\u044b\u0439\u0442\u0438", None))
        self.clear_button.setText(QCoreApplication.translate("AI_processer", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.saturation_lineEDIT.setText(QCoreApplication.translate("AI_processer", u"1.0", None))
        self.contrast_lineEDIT.setText(QCoreApplication.translate("AI_processer", u"1.0", None))
        self.preview_label.setText(QCoreApplication.translate("AI_processer", u"\u041f\u0440\u0435\u0434\u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440", None))
        self.zoom_mode_label.setText(QCoreApplication.translate("AI_processer", u"\u0420\u0435\u0436\u0438\u043c \u043c\u0430\u0441\u0448\u0442\u0430\u0431\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f:", None))
        self.quality_comboBox_image.setItemText(0, QCoreApplication.translate("AI_processer", u"No Upscale", None))
        self.quality_comboBox_image.setItemText(1, QCoreApplication.translate("AI_processer", u"2x (Normal)", None))
        self.quality_comboBox_image.setItemText(2, QCoreApplication.translate("AI_processer", u"4x (Normal)", None))
        self.quality_comboBox_image.setItemText(3, QCoreApplication.translate("AI_processer", u"4x (Anime)", None))

        self.main_tab.setTabText(self.main_tab.indexOf(self.image_tab), QCoreApplication.translate("AI_processer", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0439", None))
        self.input_output_video_groupBox.setTitle(QCoreApplication.translate("AI_processer", u"\u0412\u0432\u043e\u0434/\u0412\u044b\u0432\u043e\u0434", None))
        self.input_video_button.setText(QCoreApplication.translate("AI_processer", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0432\u0438\u0434\u0435\u043e", None))
        self.output_folder_button.setText(QCoreApplication.translate("AI_processer", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0430\u043f\u043a\u0443", None))
        self.input_video_label.setText(QCoreApplication.translate("AI_processer", u"\u0412\u0445\u043e\u0434\u043d\u043e\u0435 \u0432\u0438\u0434\u0435\u043e:", None))
        self.output_folder_label.setText(QCoreApplication.translate("AI_processer", u"\u041f\u0430\u043f\u043a\u0430 \u0432\u044b\u0432\u043e\u0434\u0430:", None))
        self.groupBox.setTitle(QCoreApplication.translate("AI_processer", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438 \u0432\u0438\u0434\u0435\u043e", None))
        self.half_precision_checkbox_video.setText(QCoreApplication.translate("AI_processer", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c Half Precision (\u0431\u044b\u0441\u0442\u0440\u0435\u0435, \u043c\u0435\u043d\u044c\u0448\u0435 VRAM, \u0442\u0440\u0435\u0431\u0443\u0435\u0442 RTX)", None))
        self.dehaze_checkbox_video.setText(QCoreApplication.translate("AI_processer", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0442\u0443\u043c\u0430\u043d (dehaze)", None))
        self.jpeg_artifacts_checkbox_video.setText(QCoreApplication.translate("AI_processer", u"\u0423\u0441\u0442\u0440\u0430\u043d\u0438\u0442\u044c JPEG-\u0430\u0440\u0442\u0435\u0444\u0430\u043a\u0442\u044b", None))
        self.sepia_checkbox_video.setText(QCoreApplication.translate("AI_processer", u"\u0421\u0442\u0438\u043b\u0438\u0437\u0430\u0446\u0438\u044f (\u0441\u0435\u043f\u0438\u044f)", None))
        self.better_faces_checkbox_video.setText(QCoreApplication.translate("AI_processer", u"\u0423\u043b\u0443\u0447\u0448\u0430\u0442\u044c \u043b\u0438\u0446\u0430", None))
        self.no_noise_checkbox_video.setText(QCoreApplication.translate("AI_processer", u"\u041f\u0440\u0435\u0434\u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 (\u0448\u0443\u043c)", None))
        self.better_colors_checkbox_video.setText(QCoreApplication.translate("AI_processer", u"\u0423\u043b\u0443\u0447\u0448\u0435\u043d\u0438\u0435 \u0446\u0432\u0435\u0442\u0430", None))
        self.contrast_sharpness_checkbox_video.setText(QCoreApplication.translate("AI_processer", u"\u041f\u043e\u0441\u0442\u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 (\u043a\u043e\u043d\u0442\u0440\u0430\u0441\u0442/\u0440\u0435\u0437\u043a\u043e\u0441\u0442\u044c)", None))
        self.better_circuits_video.setText(QCoreApplication.translate("AI_processer", u"\u0423\u0441\u0438\u043b\u0435\u043d\u0438\u0435 \u043a\u043e\u043d\u0442\u0443\u0440\u043e\u0432", None))
        self.quality_video_label.setText(QCoreApplication.translate("AI_processer", u"\u0420\u0435\u0436\u0438\u043c \u043c\u0430\u0441\u0448\u0442\u0430\u0431\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f:", None))
        self.quality_comboBox_video.setItemText(0, QCoreApplication.translate("AI_processer", u"No Upscale", None))
        self.quality_comboBox_video.setItemText(1, QCoreApplication.translate("AI_processer", u"2x (Normal)", None))
        self.quality_comboBox_video.setItemText(2, QCoreApplication.translate("AI_processer", u"3x (Anime, \u0441\u0430\u043c\u044b\u0439 \u0431\u044b\u0441\u0442\u0440\u044b\u0439 \u0438 \u0443\u043d\u0438\u0432\u0435\u0440\u0441\u0430\u043b\u044c\u043d\u044b\u0439)", None))
        self.quality_comboBox_video.setItemText(3, QCoreApplication.translate("AI_processer", u"4x (Normal)", None))
        self.quality_comboBox_video.setItemText(4, QCoreApplication.translate("AI_processer", u"4x (Anime)", None))

        self.saturation_lineEDIT_video.setText(QCoreApplication.translate("AI_processer", u"1.0", None))
        self.contrast_lineEDIT_video.setText(QCoreApplication.translate("AI_processer", u"1.0", None))
        self.saturation_label_video.setText(QCoreApplication.translate("AI_processer", u"\u041d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u043e\u0441\u0442\u044c:", None))
        self.contrast_label_video.setText(QCoreApplication.translate("AI_processer", u"\u041a\u043e\u043d\u0442\u0440\u0430\u0441\u0442:", None))
        self.output_and_perfomance_groupbox.setTitle(QCoreApplication.translate("AI_processer", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0438 \u0412\u044b\u0432\u043e\u0434", None))
        self.format_image_comboBox_2.setItemText(0, QCoreApplication.translate("AI_processer", u"PNG (default)", None))
        self.format_image_comboBox_2.setItemText(1, QCoreApplication.translate("AI_processer", u"JPEG", None))
        self.format_image_comboBox_2.setItemText(2, QCoreApplication.translate("AI_processer", u"WEBP", None))

        self.videocodec_combobox.setItemText(0, QCoreApplication.translate("AI_processer", u"H.264 (AVC)", None))
        self.videocodec_combobox.setItemText(1, QCoreApplication.translate("AI_processer", u"H.265 (HEVC)", None))
        self.videocodec_combobox.setItemText(2, QCoreApplication.translate("AI_processer", u"AV1", None))

        self.images_format_label_2.setText(QCoreApplication.translate("AI_processer", u"\u0424\u043e\u0440\u043c\u0430\u0442 \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445 \u043a\u0430\u0434\u0440\u043e\u0432:", None))
        self.image_quality_label_2.setText(QCoreApplication.translate("AI_processer", u"\u041a\u0430\u0447\u0435\u0441\u0442\u0432\u043e JPEG (75-100):", None))
        self.ffmpeg_path_label.setText(QCoreApplication.translate("AI_processer", u"\u041f\u0443\u0442\u044c \u043a FFMPEG.exe:", None))
        self.videocodec_label.setText(QCoreApplication.translate("AI_processer", u"\u0412\u0438\u0434\u0435\u043e\u043a\u043e\u0434\u0435\u043a:", None))
        self.quality_crf_label.setText(QCoreApplication.translate("AI_processer", u"\u041a\u0430\u0447\u0435\u0441\u0442\u0432\u043e/CRF (0-51 \u0434\u043b\u044f x264/x265, 1-51 \u0434\u043b\u044f NVENC CQP):", None))
        self.ffmpeg_path_button.setText(QCoreApplication.translate("AI_processer", u"\u041e\u0431\u0437\u043e\u0440...", None))
        self.ffmpeg_download_button.setText(QCoreApplication.translate("AI_processer", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c", None))
        self.remove_black_lines_from_upscale_checkbox.setText(QCoreApplication.translate("AI_processer", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0447\u0435\u0440\u043d\u044b\u0435 \u043f\u043e\u043b\u043e\u0441\u044b", None))
        self.remove_metainfo_from_upscale_checkbox.setText(QCoreApplication.translate("AI_processer", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.keep_fps_checkbox.setText(QCoreApplication.translate("AI_processer", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0441\u0445\u043e\u0434\u043d\u044b\u0439 FPS", None))
        self.remove_audio_checkbox.setText(QCoreApplication.translate("AI_processer", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0432\u0443\u043a", None))
        self.status_video_label.setText(QCoreApplication.translate("AI_processer", u"\u0421\u0442\u0430\u0442\u0443\u0441: \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u0435", None))
        self.start_processing_video_button.setText(QCoreApplication.translate("AI_processer", u"\u041d\u0430\u0447\u0430\u0442\u044c \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0443", None))
        self.stop_processing_video_button.setText(QCoreApplication.translate("AI_processer", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0438 \u0432\u044b\u0439\u0442\u0438", None))
        self.clear_logs_button.setText(QCoreApplication.translate("AI_processer", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0432\u044b\u0432\u043e\u0434", None))
        self.main_tab.setTabText(self.main_tab.indexOf(self.video_tab), QCoreApplication.translate("AI_processer", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u0432\u0438\u0434\u0435\u043e", None))
        self.input_output_video_groupBox_2.setTitle(QCoreApplication.translate("AI_processer", u"\u0412\u0432\u043e\u0434/\u0412\u044b\u0432\u043e\u0434", None))
        self.input_video_button_2.setText(QCoreApplication.translate("AI_processer", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0432\u0438\u0434\u0435\u043e", None))
        self.output_folder_button_2.setText(QCoreApplication.translate("AI_processer", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0430\u043f\u043a\u0443", None))
        self.input_video_label_3.setText(QCoreApplication.translate("AI_processer", u"\u0412\u0445\u043e\u0434\u043d\u043e\u0435 \u0432\u0438\u0434\u0435\u043e:", None))
        self.output_folder_label_3.setText(QCoreApplication.translate("AI_processer", u"\u041f\u0430\u043f\u043a\u0430 \u0432\u044b\u0432\u043e\u0434\u0430:", None))
        self.log_textEDIT_3.setHtml(QCoreApplication.translate("AI_processer", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; color:#d1c40b;\">\u26a0\ufe0f ATTENTION \u26a0\ufe0f</span><span style=\" font-size:28pt;\"><br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt;\">\u2757\u2757\u2757</span><span style=\" font-size:28pt; color:#a81a1c;\"> </span></p>\n"
"<p style=\" mar"
                        "gin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; color:#a81a1c;\">FPS GENERATING IN BETA </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; color:#a81a1c;\">IT MAY BE UNSTABLE </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; color:#a81a1c;\">\u2757\u2757\u2757</span></p></body></html>", None))
        self.status_video_label_3.setText(QCoreApplication.translate("AI_processer", u"\u0421\u0442\u0430\u0442\u0443\u0441: \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u0435", None))
        self.frames_to_interpolate_label.setText(QCoreApplication.translate("AI_processer", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u0434\u043e\u0440\u0438\u0441\u043e\u0432\u043a\u0438 \u043a\u0430\u0434\u0440\u043e\u0432:", None))
        self.frames_to_interpolate_comboBox.setItemText(0, QCoreApplication.translate("AI_processer", u"2x (\u0421\u0442\u0430\u043d\u0434\u0430\u0440\u0442, \u0431\u044b\u0441\u0442\u0440\u0430\u044f \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c)", None))
        self.frames_to_interpolate_comboBox.setItemText(1, QCoreApplication.translate("AI_processer", u"4x", None))
        self.frames_to_interpolate_comboBox.setItemText(2, QCoreApplication.translate("AI_processer", u"6x", None))
        self.frames_to_interpolate_comboBox.setItemText(3, QCoreApplication.translate("AI_processer", u"8x", None))

        self.output_and_perfomance_groupbox_2.setTitle(QCoreApplication.translate("AI_processer", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0438 \u0412\u044b\u0432\u043e\u0434", None))
        self.format_image_comboBox_4.setItemText(0, QCoreApplication.translate("AI_processer", u"PNG (default)", None))
        self.format_image_comboBox_4.setItemText(1, QCoreApplication.translate("AI_processer", u"JPEG", None))
        self.format_image_comboBox_4.setItemText(2, QCoreApplication.translate("AI_processer", u"WEBP", None))

        self.videocodec_combobox_2.setItemText(0, QCoreApplication.translate("AI_processer", u"H.264 (AVC)", None))
        self.videocodec_combobox_2.setItemText(1, QCoreApplication.translate("AI_processer", u"H.265 (HEVC)", None))
        self.videocodec_combobox_2.setItemText(2, QCoreApplication.translate("AI_processer", u"AV1", None))

        self.images_format_label_3.setText(QCoreApplication.translate("AI_processer", u"\u0424\u043e\u0440\u043c\u0430\u0442 \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445 \u043a\u0430\u0434\u0440\u043e\u0432:", None))
        self.image_quality_label_4.setText(QCoreApplication.translate("AI_processer", u"\u041a\u0430\u0447\u0435\u0441\u0442\u0432\u043e JPEG (75-100):", None))
        self.ffmpeg_path_label_2.setText(QCoreApplication.translate("AI_processer", u"\u041f\u0443\u0442\u044c \u043a FFMPEG.exe:", None))
        self.videocodec_label_2.setText(QCoreApplication.translate("AI_processer", u"\u0412\u0438\u0434\u0435\u043e\u043a\u043e\u0434\u0435\u043a:", None))
        self.quality_crf_label_2.setText(QCoreApplication.translate("AI_processer", u"\u041a\u0430\u0447\u0435\u0441\u0442\u0432\u043e/CRF (0-51 \u0434\u043b\u044f x264/x265, 1-51 \u0434\u043b\u044f NVENC CQP):", None))
        self.ffmpeg_path_button_2.setText(QCoreApplication.translate("AI_processer", u"\u041e\u0431\u0437\u043e\u0440...", None))
        self.ffmpeg_download_button_2.setText(QCoreApplication.translate("AI_processer", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c", None))
        self.remove_black_lines_checkbox.setText(QCoreApplication.translate("AI_processer", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0447\u0435\u0440\u043d\u044b\u0435 \u043f\u043e\u043b\u043e\u0441\u044b", None))
        self.remove_metainfo_checkbox.setText(QCoreApplication.translate("AI_processer", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.remove_audio_checkbox_2.setText(QCoreApplication.translate("AI_processer", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0432\u0443\u043a", None))
        self.start_processing_frames_button.setText(QCoreApplication.translate("AI_processer", u"\u041d\u0430\u0447\u0430\u0442\u044c \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0443", None))
        self.stop_processing_frames_button.setText(QCoreApplication.translate("AI_processer", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0438 \u0432\u044b\u0439\u0442\u0438", None))
        self.clear_frame_output_button.setText(QCoreApplication.translate("AI_processer", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0432\u044b\u0432\u043e\u0434", None))
        self.main_tab.setTabText(self.main_tab.indexOf(self.generating_frames_tab), QCoreApplication.translate("AI_processer", u"\u0414\u043e\u0440\u0438\u0441\u043e\u0432\u043a\u0430 \u043a\u0430\u0434\u0440\u043e\u0432", None))
        self.cuda_info_groopbox.setTitle(QCoreApplication.translate("AI_processer", u"\u0421\u0442\u0430\u0442\u0443\u0441 CUDA", None))
        self.cuda_devices_label.setText(QCoreApplication.translate("AI_processer", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432 CUDA: 0", None))
        self.cuda_mode.setText(QCoreApplication.translate("AI_processer", u"<html><head/><body><p><span style=\" font-weight:700;\">\u0420\u0435\u0436\u0438\u043c \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438:</span></p></body></html>", None))
        self.gp_cuda_info_label.setText(QCoreApplication.translate("AI_processer", u"<html><head/><body><p><span style=\" font-weight:700; color:#b40508;\">\u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0431\u0443\u0434\u0435\u0442 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0426\u041f \u0434\u043b\u044f \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438.</span></p></body></html>", None))
        self.cuda_accessibility_label.setText(QCoreApplication.translate("AI_processer", u"<html><head/><body><p><span style=\" font-weight:700;\">\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u0441\u0442\u044c CUDA:</span></p></body></html>", None))
        self.cuda_status_label.setText(QCoreApplication.translate("AI_processer", u"<html><head/><body><p><span style=\" font-weight:700; color:#b40508;\">\u041d\u0435\u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e</span></p></body></html>", None))
        self.cuda_information_label.setText(QCoreApplication.translate("AI_processer", u"<html><head/><body><p><span style=\" font-weight:700;\">\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e\u0431 \u0443\u0441\u0442\u0440\u043e\u0441\u0442\u0432\u0435(\u0430\u0445) CUDA:</span></p></body></html>", None))
        self.cuda_update_pushButton.setText(QCoreApplication.translate("AI_processer", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.interpolation_info_groupbox.setTitle(QCoreApplication.translate("AI_processer", u"\u041e\u0431 \u0438\u043d\u0442\u0435\u0440\u043f\u043e\u043b\u044f\u0446\u0438\u0438", None))
        self.interpolation_info_label.setText(QCoreApplication.translate("AI_processer", u"<html><head/><body><p><span style=\" font-weight:700; color:#c2c2c2;\">\u0418\u043d\u0442\u0435\u0440\u043f\u043e\u043b\u044f\u0446\u0438\u044f \u043a\u0430\u0434\u0440\u043e\u0432</span> \u2014 \u044d\u0442\u043e \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u044f, \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u044e\u0449\u0430\u044f \u0441\u043e\u0437\u0434\u0430\u0432\u0430\u0442\u044c \u043f\u0440\u043e\u043c\u0435\u0436\u0443\u0442\u043e\u0447\u043d\u044b\u0435 \u043a\u0430\u0434\u0440\u044b \u043c\u0435\u0436\u0434\u0443 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u043c\u0438, \u0442\u0435\u043c \u0441\u0430\u043c\u044b\u043c \u0443\u0432\u0435\u043b\u0438\u0447\u0438\u0432\u0430\u044f \u0447\u0430\u0441\u0442\u043e\u0442\u0443 </p><p>\u043a\u0430\u0434\u0440\u043e\u0432 \u0432\u0438\u0434\u0435\u043e. \u042d\u0442\u043e \u0434\u0435\u043b\u0430\u0435\u0442 \u0432\u0438\u0434\u0435\u043e \u0431\u043e\u043b\u0435\u0435 \u043f\u043b\u0430\u0432\u043d\u044b\u043c, \u043e\u0441\u043e"
                        "\u0431\u0435\u043d\u043d\u043e \u0437\u0430\u043c\u0435\u0442\u043d\u043e \u043f\u0440\u0438 \u0437\u0430\u043c\u0435\u0434\u043b\u0435\u043d\u043d\u043e\u043c \u0432\u043e\u0441\u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u0438\u043b\u0438 \u043f\u0440\u0438 \u043f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0438 \u0432\u0438\u0434\u0435\u043e </p><p>\u0441 \u043d\u0438\u0437\u043a\u0438\u043c <span style=\" font-weight:700;\">FPS </span>\u0432 \u0431\u043e\u043b\u0435\u0435 \u0432\u044b\u0441\u043e\u043a\u043e\u0435.</p><p><br/></p><p><span style=\" font-style:italic;\">\u0412 \u043c\u043e\u0435\u043c \u043f\u0440\u043e\u0435\u043a\u0442\u0435 \u0434\u043b\u044f \u0438\u043d\u0442\u0435\u0440\u043f\u043e\u043b\u044f\u0446\u0438\u0438 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c </span><span style=\" font-weight:700; font-style:italic; color:#bebebe;\">RIFE</span><span style=\""
                        " font-style:italic;\"> (Real-Time Intermediate Flow Estimation). \u042d\u0442\u043e \u0441\u043e\u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0439 \u043c\u0435\u0442\u043e\u0434 </span></p><p><span style=\" font-style:italic;\">\u0438\u043d\u0442\u0435\u0440\u043f\u043e\u043b\u044f\u0446\u0438\u0438 \u043d\u0430 \u043e\u0441\u043d\u043e\u0432\u0435 \u043d\u0435\u0439\u0440\u043e\u0441\u0435\u0442\u0435\u0439, \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043d\u044b\u0439 \u0434\u043b\u044f \u0433\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u0438 \u043f\u0440\u043e\u043c\u0435\u0436\u0443\u0442\u043e\u0447\u043d\u044b\u0445 \u043a\u0430\u0434\u0440\u043e\u0432 \u0441 \u0432\u044b\u0441\u043e\u043a\u043e\u0439 \u0442\u043e\u0447\u043d\u043e\u0441\u0442\u044c\u044e \u0438 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e\u043c.<br/><br/><br/><br/></span></p></body></html>", None))
        self.gifLabelI2.setText("")
        self.gifLabelD2.setText("")
        self.main_tab.setTabText(self.main_tab.indexOf(self.program_info_tab), QCoreApplication.translate("AI_processer", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.language_label.setText(QCoreApplication.translate("AI_processer", u"\u042f\u0437\u044b\u043a:", None))
        self.language_comboBox.setItemText(0, QCoreApplication.translate("AI_processer", u"English", None))
        self.language_comboBox.setItemText(1, QCoreApplication.translate("AI_processer", u"\u0420\u0443\u0441\u0441\u043a\u0438\u0439", None))

        self.model_status_label.setText(QCoreApplication.translate("AI_processer", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.model_status_badge_label.setText(QCoreApplication.translate("AI_processer", u"<html><head/><body><p>badge</p></body></html>", None))
        self.dark_theme_radio.setText(QCoreApplication.translate("AI_processer", u"Dark", None))
        self.light_theme_radio.setText(QCoreApplication.translate("AI_processer", u"Light", None))
        self.castle_theme_radio.setText(QCoreApplication.translate("AI_processer", u"Castle", None))
        self.theme_pushButton.setText(QCoreApplication.translate("AI_processer", u"Glass mode", None))
    # retranslateUi

