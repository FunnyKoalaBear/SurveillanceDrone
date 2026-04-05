# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1052, 710)
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet(u"/* 1. Global Background and Text */\n"
"QMainWindow, QWidget {\n"
"    background-color: #121212; /* Deep dark grey/black */\n"
"    color: #E0E0E0; /* Off-white text for readability */\n"
"    font-family: \"Segoe UI\", \"Helvetica Neue\", sans-serif;\n"
"}\n"
"\n"
"/* 2. Layout Panels (Your QFrames) */\n"
"QFrame {\n"
"    background-color: #1E1E24; /* Slightly lighter grey for panels */\n"
"    border: 1px solid #2A2A35;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"/* 3. The Video Feed Label */\n"
"/* Assuming you name your camera label \"video_feed_label\" */\n"
"QLabel#video_feed_label {\n"
"    background-color: #000000;\n"
"    border: 2px solid #00F3FF; /* Neon Cyan tactical border */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* 4. Standard Text Labels (Telemetry data) */\n"
"QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"/* 5. Modern Interactive Buttons */\n"
"QPushButton {\n"
"    background-color: #2D2D3A;\n"
"    border: 1px solid #00F3F"
                        "F; /* Cyan outline */\n"
"    color: #00F3FF; /* Cyan text */\n"
"    padding: 8px 16px;\n"
"    border-radius: 4px;\n"
"    font-weight: bold;\n"
"	font: bold 11pt \"Ubuntu Sans\";\n"
"\n"
"    letter-spacing: 1px;\n"
"}\n"
"\n"
"/* Button Hover Animation */\n"
"QPushButton:hover {\n"
"    background-color: #00F3FF; /* Fill solid cyan on hover */\n"
"    color: #121212; /* Invert text to black */\n"
"}\n"
"\n"
"/* Button Click Animation */\n"
"QPushButton:pressed {\n"
"    background-color: #00B8D4;\n"
"    border: 1px solid #00B8D4;\n"
"}\n"
"\n"
"/* 6. The Console Output (Read-only text box) */\n"
"QTextEdit {\n"
"    background-color: #0A0A0C; /* Pitch black */\n"
"    color: #00FF41; /* Hacker terminal green */\n"
"    border: 1px solid #2A2A35;\n"
"    font-family: \"Courier New\", monospace;\n"
"    padding: 10px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* General Text Labels (For titles like \"Battery\", \"Altitude\") */\n"
"QLabel {\n"
"    background-color: #1A1A24; /* Slightly lighter than the ba"
                        "ckground */\n"
"    color: #A0A0B0; /* Muted grey/white text so it isn't blinding */\n"
"    padding: 6px 12px;\n"
"    border-radius: 4px;\n"
"    font-size: 13px;\n"
"    border-left: 3px solid #2A2A35; /* Subtle grey edge to give it structure */\n"
"}\n"
"\n"
"\n"
"/* 1. GroupBox Main Body (The Secret Fix) */\n"
"QGroupBox {\n"
"    color: #00F3FF;\n"
"    border: 1px solid #2A2A35;\n"
"    border-radius: 6px;\n"
"    margin-top: 25px; \n"
"    \n"
"    /* Apply the massive font to the WHOLE box so the title inherits it */\n"
"    font:  16pt \"Ubuntu Sans\"; \n"
"}\n"
"\n"
"/* 2. GroupBox Title Alignment */\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: top left;\n"
"    padding: 0 8px; \n"
"    left: 1px; \n"
"    background-color: #1E1E24; \n"
"    /* Notice: No font commands here anymore! */\n"
"}\n"
"\n"
"/* 3. GroupBox Data Labels */\n"
"QGroupBox QLabel {\n"
"    /* Force the labels back down so they don't stay giant */\n"
"    font: 12pt \"Ubuntu Sans\";\n"
""
                        "    font-weight: normal; \n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_right = QFrame(self.centralwidget)
        self.frame_right.setObjectName(u"frame_right")
        self.frame_right.setMinimumSize(QSize(291, 0))
        self.frame_right.setMaximumSize(QSize(291, 16777215))
        self.frame_right.setBaseSize(QSize(100, 0))
        self.frame_right.setFrameShape(QFrame.StyledPanel)
        self.frame_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_right)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.frame_right)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_7 = QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.dock_button = QPushButton(self.groupBox)
        self.dock_button.setObjectName(u"dock_button")

        self.gridLayout_7.addWidget(self.dock_button, 0, 0, 1, 1)

        self.toggle_claw_button = QPushButton(self.groupBox)
        self.toggle_claw_button.setObjectName(u"toggle_claw_button")

        self.gridLayout_7.addWidget(self.toggle_claw_button, 0, 1, 1, 1)

        self.radar_label = QLabel(self.groupBox)
        self.radar_label.setObjectName(u"radar_label")
        self.radar_label.setMinimumSize(QSize(0, 40))
        self.radar_label.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_7.addWidget(self.radar_label, 1, 0, 1, 1)

        self.claw_current_label = QLabel(self.groupBox)
        self.claw_current_label.setObjectName(u"claw_current_label")
        self.claw_current_label.setMinimumSize(QSize(0, 40))
        self.claw_current_label.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_7.addWidget(self.claw_current_label, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame_right)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.speak_button = QPushButton(self.groupBox_2)
        self.speak_button.setObjectName(u"speak_button")

        self.verticalLayout_4.addWidget(self.speak_button)

        self.speak_status = QLabel(self.groupBox_2)
        self.speak_status.setObjectName(u"speak_status")
        self.speak_status.setMinimumSize(QSize(0, 40))
        self.speak_status.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_4.addWidget(self.speak_status)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.frame_right)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.co2_label = QLabel(self.groupBox_3)
        self.co2_label.setObjectName(u"co2_label")
        self.co2_label.setMinimumSize(QSize(0, 40))
        self.co2_label.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_5.addWidget(self.co2_label, 0, 0, 1, 1)

        self.vo2_label = QLabel(self.groupBox_3)
        self.vo2_label.setObjectName(u"vo2_label")
        self.vo2_label.setMinimumSize(QSize(0, 40))
        self.vo2_label.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_5.addWidget(self.vo2_label, 0, 1, 1, 1)

        self.hum_label = QLabel(self.groupBox_3)
        self.hum_label.setObjectName(u"hum_label")
        self.hum_label.setMinimumSize(QSize(0, 40))
        self.hum_label.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_5.addWidget(self.hum_label, 1, 0, 1, 1)

        self.temp_label = QLabel(self.groupBox_3)
        self.temp_label.setObjectName(u"temp_label")
        self.temp_label.setMinimumSize(QSize(0, 40))
        self.temp_label.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_5.addWidget(self.temp_label, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.gridLayout_2.addWidget(self.frame_right, 0, 3, 1, 1)

        self.frame_center = QFrame(self.centralwidget)
        self.frame_center.setObjectName(u"frame_center")
        self.frame_center.setFrameShape(QFrame.StyledPanel)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_center)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.alert = QLabel(self.frame_center)
        self.alert.setObjectName(u"alert")
        self.alert.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.alert)

        self.video_frame = QLabel(self.frame_center)
        self.video_frame.setObjectName(u"video_frame")

        self.verticalLayout.addWidget(self.video_frame)

        self.log = QTextEdit(self.frame_center)
        self.log.setObjectName(u"log")
        self.log.setMinimumSize(QSize(0, 50))
        self.log.setMaximumSize(QSize(16777215, 180))
        self.log.setReadOnly(True)

        self.verticalLayout.addWidget(self.log)


        self.gridLayout_2.addWidget(self.frame_center, 0, 2, 1, 1)

        self.frame_left = QFrame(self.centralwidget)
        self.frame_left.setObjectName(u"frame_left")
        self.frame_left.setMinimumSize(QSize(291, 0))
        self.frame_left.setMaximumSize(QSize(291, 16777215))
        self.frame_left.setBaseSize(QSize(100, 0))
        self.frame_left.setFrameShape(QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_left)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.telem_box = QGroupBox(self.frame_left)
        self.telem_box.setObjectName(u"telem_box")
        self.gridLayout_3 = QGridLayout(self.telem_box)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.battery_label = QLabel(self.telem_box)
        self.battery_label.setObjectName(u"battery_label")
        self.battery_label.setMaximumSize(QSize(16777215, 40))
        self.battery_label.setBaseSize(QSize(40, 0))

        self.gridLayout_3.addWidget(self.battery_label, 0, 0, 1, 1)

        self.current_label = QLabel(self.telem_box)
        self.current_label.setObjectName(u"current_label")
        self.current_label.setMaximumSize(QSize(16777215, 40))
        self.current_label.setBaseSize(QSize(40, 0))

        self.gridLayout_3.addWidget(self.current_label, 0, 1, 1, 1)

        self.altitude_label = QLabel(self.telem_box)
        self.altitude_label.setObjectName(u"altitude_label")
        self.altitude_label.setMaximumSize(QSize(16777215, 40))
        self.altitude_label.setBaseSize(QSize(40, 0))

        self.gridLayout_3.addWidget(self.altitude_label, 1, 0, 1, 1)

        self.velocity_label = QLabel(self.telem_box)
        self.velocity_label.setObjectName(u"velocity_label")
        self.velocity_label.setMaximumSize(QSize(16777215, 40))
        self.velocity_label.setBaseSize(QSize(40, 0))

        self.gridLayout_3.addWidget(self.velocity_label, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.telem_box, 4, 0, 1, 2)

        self.system_box = QGroupBox(self.frame_left)
        self.system_box.setObjectName(u"system_box")
        self.gridLayout_4 = QGridLayout(self.system_box)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.audio_alert_label = QLabel(self.system_box)
        self.audio_alert_label.setObjectName(u"audio_alert_label")
        self.audio_alert_label.setMaximumSize(QSize(16777215, 40))
        self.audio_alert_label.setBaseSize(QSize(40, 0))

        self.gridLayout_4.addWidget(self.audio_alert_label, 1, 1, 1, 1)

        self.video_alert_label = QLabel(self.system_box)
        self.video_alert_label.setObjectName(u"video_alert_label")
        self.video_alert_label.setMaximumSize(QSize(16777215, 40))
        self.video_alert_label.setBaseSize(QSize(40, 0))

        self.gridLayout_4.addWidget(self.video_alert_label, 1, 0, 1, 1)

        self.recording_label = QLabel(self.system_box)
        self.recording_label.setObjectName(u"recording_label")
        self.recording_label.setMaximumSize(QSize(16777215, 40))
        self.recording_label.setBaseSize(QSize(40, 0))

        self.gridLayout_4.addWidget(self.recording_label, 0, 1, 1, 1)

        self.armed_label = QLabel(self.system_box)
        self.armed_label.setObjectName(u"armed_label")
        self.armed_label.setMaximumSize(QSize(16777215, 40))
        self.armed_label.setBaseSize(QSize(40, 0))

        self.gridLayout_4.addWidget(self.armed_label, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.system_box, 5, 0, 1, 2)

        self.ARM_button = QPushButton(self.frame_left)
        self.ARM_button.setObjectName(u"ARM_button")

        self.gridLayout.addWidget(self.ARM_button, 2, 0, 1, 1)

        self.HOLD_button = QPushButton(self.frame_left)
        self.HOLD_button.setObjectName(u"HOLD_button")

        self.gridLayout.addWidget(self.HOLD_button, 2, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.app_logo = QLabel(self.frame_left)
        self.app_logo.setObjectName(u"app_logo")
        self.app_logo.setPixmap(QPixmap(u"../../../../.designer/backup/img/drone.png"))
        self.app_logo.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.app_logo, 0, Qt.AlignHCenter)

        self.label_app_title = QLabel(self.frame_left)
        self.label_app_title.setObjectName(u"label_app_title")
        self.label_app_title.setStyleSheet(u"/* Branding / App Title Styling */\n"
"QLabel {\n"
"    color: #00F3FF; /* Cyan to match your accent colors */\n"
"    font: bold 8pt \"Ubuntu Sans\";\n"
"    background-color: transparent; /* Ensures no weird boxes */\n"
"    border: none; /* Removes any default borders */\n"
"    border-top: 1px solid #2A2A35; /* Creates a subtle line separating the logo from the spacer */\n"
"    padding-top: 15px; /* Pushes the text down away from the line */\n"
"    padding-bottom: 5px;\n"
"    qproperty-alignment: AlignCenter; /* Forces the text perfectly to the center */\n"
"    letter-spacing: 2px; /* Spreads the letters out for a cinematic, high-tech look */\n"
"}")

        self.verticalLayout_2.addWidget(self.label_app_title)


        self.gridLayout_2.addWidget(self.frame_left, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1052, 26))
        self.log_out = QMenu(self.menubar)
        self.log_out.setObjectName(u"log_out")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.log_out.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"CLAW", None))
        self.dock_button.setText(QCoreApplication.translate("MainWindow", u"Dock", None))
        self.toggle_claw_button.setText(QCoreApplication.translate("MainWindow", u"Toggle", None))
        self.radar_label.setText(QCoreApplication.translate("MainWindow", u"Radar", None))
        self.claw_current_label.setText(QCoreApplication.translate("MainWindow", u"Claw Current", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Voice", None))
        self.speak_button.setText(QCoreApplication.translate("MainWindow", u"SPEAK", None))
        self.speak_status.setText(QCoreApplication.translate("MainWindow", u"Status: Disabled", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Enviroment", None))
        self.co2_label.setText(QCoreApplication.translate("MainWindow", u"CO2", None))
        self.vo2_label.setText(QCoreApplication.translate("MainWindow", u"VO2", None))
        self.hum_label.setText(QCoreApplication.translate("MainWindow", u"Humidity", None))
        self.temp_label.setText(QCoreApplication.translate("MainWindow", u"Temp", None))
        self.alert.setText(QCoreApplication.translate("MainWindow", u"Alert : Error 303. Please finish developing this application", None))
        self.video_frame.setText(QCoreApplication.translate("MainWindow", u"video_frame", None))
        self.log.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Courier New','monospace'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Log: </p></body></html>", None))
        self.telem_box.setTitle(QCoreApplication.translate("MainWindow", u"TELEM", None))
        self.battery_label.setText(QCoreApplication.translate("MainWindow", u"Battery", None))
        self.current_label.setText(QCoreApplication.translate("MainWindow", u"Current Draw", None))
        self.altitude_label.setText(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.velocity_label.setText(QCoreApplication.translate("MainWindow", u"Velocity", None))
        self.system_box.setTitle(QCoreApplication.translate("MainWindow", u"System Status", None))
        self.audio_alert_label.setText(QCoreApplication.translate("MainWindow", u"Audio Alert", None))
        self.video_alert_label.setText(QCoreApplication.translate("MainWindow", u"Video Alert", None))
        self.recording_label.setText(QCoreApplication.translate("MainWindow", u"Recording", None))
        self.armed_label.setText(QCoreApplication.translate("MainWindow", u"ARMED", None))
        self.ARM_button.setText(QCoreApplication.translate("MainWindow", u"ARM", None))
        self.HOLD_button.setText(QCoreApplication.translate("MainWindow", u"HOLD", None))
        self.app_logo.setText("")
        self.label_app_title.setText(QCoreApplication.translate("MainWindow", u"Drone Surveillance Application", None))
        self.log_out.setTitle(QCoreApplication.translate("MainWindow", u"Log out", None))
    # retranslateUi

