# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainAiJsaa.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(359, 426)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(319, 295))
        MainWindow.setMaximumSize(QSize(359, 426))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        brush2 = QBrush(QColor(127, 127, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
        brush3 = QBrush(QColor(170, 170, 170, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush4 = QBrush(QColor(255, 255, 220, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 128))
        brush5.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"IRANYekan")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        MainWindow.setAcceptDrops(False)
        MainWindow.setLayoutDirection(Qt.RightToLeft)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Version_Text = QLabel(self.centralwidget)
        self.Version_Text.setObjectName(u"Version_Text")
        self.Version_Text.setGeometry(QRect(160, 380, 41, 16))
        font1 = QFont()
        font1.setFamily(u"IRANYekan")
        font1.setPointSize(7)
        font1.setBold(False)
        font1.setWeight(50)
        self.Version_Text.setFont(font1)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 361, 261))
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setMovable(False)
        self.OG = QWidget()
        self.OG.setObjectName(u"OG")
        self.OpenGamesBtn = QPushButton(self.OG)
        self.OpenGamesBtn.setObjectName(u"OpenGamesBtn")
        self.OpenGamesBtn.setGeometry(QRect(200, 20, 141, 51))
        self.OpenGamesBtn.setFont(font)
        self.OpenGamesBtn.setStyleSheet(u"QPushButton#OpenGamesBtn {\n"
"    background: #f5f5fa;\n"
"    border: 0;\n"
"    border-radius: 8px;\n"
"    box-shadow: -10px -10px 30px 0 #fff, 10px 10px 30px 0 rgba(29, 13, 202, 0.09);\n"
"    color: #2a1f62;\n"
"    cursor: pointer;\n"
"    padding: 15px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton#OpenGamesBtn:hover {\n"
"    background: #f8f8ff;\n"
"    box-shadow: -15px -15px 30px 0 #fff, 15px 15px 30px 0 rgba(29, 13, 202, 0.09);\n"
"}\n"
"\n"
"QPushButton#OpenGamesBtn:pressed {\n"
"    background: #f5f5fa;\n"
"    box-shadow: inset -5px -5px 10px 0 #fff, inset 5px 5px 10px 0 rgba(29, 13, 202, 0.09);\n"
"}\n"
"\n"
"@media (min-width: 768px) {\n"
"    QPushButton#OpenGamesBtn {\n"
"        padding: 24px;\n"
"    }\n"
"}\n"
"")
        self.SteamDBCheck = QCheckBox(self.OG)
        self.SteamDBCheck.setObjectName(u"SteamDBCheck")
        self.SteamDBCheck.setGeometry(QRect(70, 20, 91, 20))
        self.VarsCheck = QCheckBox(self.OG)
        self.VarsCheck.setObjectName(u"VarsCheck")
        self.VarsCheck.setGeometry(QRect(20, 50, 141, 20))
        self.LinkForOpen_Input = QTextEdit(self.OG)
        self.LinkForOpen_Input.setObjectName(u"LinkForOpen_Input")
        self.LinkForOpen_Input.setGeometry(QRect(10, 120, 331, 41))
        font2 = QFont()
        font2.setFamily(u"IRANYekan")
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setWeight(50)
        self.LinkForOpen_Input.setFont(font2)
        self.line = QFrame(self.OG)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 80, 331, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.G_name_label = QLabel(self.OG)
        self.G_name_label.setObjectName(u"G_name_label")
        self.G_name_label.setGeometry(QRect(280, 90, 55, 21))
        self.OpenGame_SingleBtn = QPushButton(self.OG)
        self.OpenGame_SingleBtn.setObjectName(u"OpenGame_SingleBtn")
        self.OpenGame_SingleBtn.setGeometry(QRect(120, 170, 121, 41))
        self.OpenGame_SingleBtn.setFont(font)
        self.OpenGame_SingleBtn.setStyleSheet(u"QPushButton#OpenGame_SingleBtn {\n"
"    background: #f5f5fa;\n"
"    border: 0;\n"
"    border-radius: 8px;\n"
"    box-shadow: -10px -10px 30px 0 #fff, 10px 10px 30px 0 rgba(29, 13, 202, 0.09);\n"
"    color: #2a1f62;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton#OpenGame_SingleBtn:hover {\n"
"    background: #f8f8ff;\n"
"    box-shadow: -15px -15px 30px 0 #fff, 15px 15px 30px 0 rgba(29, 13, 202, 0.09);\n"
"}\n"
"\n"
"QPushButton#OpenGame_SingleBtn:pressed {\n"
"    background: #f5f5fa;\n"
"    box-shadow: inset -5px -5px 10px 0 #fff, inset 5px 5px 10px 0 rgba(29, 13, 202, 0.09);\n"
"}\n"
"\n"
"@media (min-width: 768px) {\n"
"    QPushButton#OpenGame_SingleBtn {\n"
"        padding: 24px;\n"
"    }\n"
"}\n"
"")
        self.tabWidget.addTab(self.OG, "")
        self.HA = QWidget()
        self.HA.setObjectName(u"HA")
        self.RemoveDiscBtn = QPushButton(self.HA)
        self.RemoveDiscBtn.setObjectName(u"RemoveDiscBtn")
        self.RemoveDiscBtn.setGeometry(QRect(200, 20, 141, 51))
        self.RemoveDiscBtn.setFont(font)
        self.RemoveDiscBtn.setStyleSheet(u"QPushButton#RemoveDiscBtn {\n"
"    background: #f5f5fa;\n"
"    border: 0;\n"
"    border-radius: 8px;\n"
"    box-shadow: -10px -10px 30px 0 #fff, 10px 10px 30px 0 rgba(29, 13, 202, 0.09);\n"
"    color: #2a1f62;\n"
"    cursor: pointer;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton#RemoveDiscBtn:hover {\n"
"    background: #f8f8ff;\n"
"    box-shadow: -15px -15px 30px 0 #fff, 15px 15px 30px 0 rgba(29, 13, 202, 0.09);\n"
"}\n"
"\n"
"QPushButton#RemoveDiscBtn:pressed {\n"
"    background: #f5f5fa;\n"
"    box-shadow: inset -5px -5px 10px 0 #fff, inset 5px 5px 10px 0 rgba(29, 13, 202, 0.09);\n"
"}\n"
"\n"
"@media (min-width: 768px) {\n"
"    QPushButton#RemoveDiscBtn {\n"
"        padding: 24px;\n"
"    }\n"
"}\n"
"")
        self.G_name_label_2 = QLabel(self.HA)
        self.G_name_label_2.setObjectName(u"G_name_label_2")
        self.G_name_label_2.setGeometry(QRect(280, 90, 55, 21))
        self.LinkForOpen_Input_2 = QTextEdit(self.HA)
        self.LinkForOpen_Input_2.setObjectName(u"LinkForOpen_Input_2")
        self.LinkForOpen_Input_2.setGeometry(QRect(10, 120, 331, 41))
        self.LinkForOpen_Input_2.setFont(font2)
        self.line_2 = QFrame(self.HA)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 80, 331, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.RemoveDisc_SingleBtn = QPushButton(self.HA)
        self.RemoveDisc_SingleBtn.setObjectName(u"RemoveDisc_SingleBtn")
        self.RemoveDisc_SingleBtn.setGeometry(QRect(110, 170, 141, 41))
        self.RemoveDisc_SingleBtn.setFont(font)
        self.RemoveDisc_SingleBtn.setStyleSheet(u"QPushButton#RemoveDisc_SingleBtn {\n"
"    background: #f5f5fa;\n"
"    border: 0;\n"
"    border-radius: 8px;\n"
"    box-shadow: -10px -10px 30px 0 #fff, 10px 10px 30px 0 rgba(29, 13, 202, 0.09);\n"
"    color: #2a1f62;\n"
"    cursor: pointer;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton#RemoveDisc_SingleBtn:hover {\n"
"    background: #f8f8ff;\n"
"    box-shadow: -15px -15px 30px 0 #fff, 15px 15px 30px 0 rgba(29, 13, 202, 0.09);\n"
"}\n"
"\n"
"QPushButton#RemoveDisc_SingleBtn:pressed {\n"
"    background: #f5f5fa;\n"
"    box-shadow: inset -5px -5px 10px 0 #fff, inset 5px 5px 10px 0 rgba(29, 13, 202, 0.09);\n"
"}\n"
"\n"
"@media (min-width: 768px) {\n"
"    QPushButton#RemoveDisc_SingleBtn {\n"
"        padding: 24px;\n"
"    }\n"
"}\n"
"")
        self.OnScreenRemCheck = QCheckBox(self.HA)
        self.OnScreenRemCheck.setObjectName(u"OnScreenRemCheck")
        self.OnScreenRemCheck.setGeometry(QRect(10, 180, 91, 20))
        self.MultiRemCheck = QCheckBox(self.HA)
        self.MultiRemCheck.setObjectName(u"MultiRemCheck")
        self.MultiRemCheck.setGeometry(QRect(10, 20, 111, 20))
        self.MultiRemCounter = QSpinBox(self.HA)
        self.MultiRemCounter.setObjectName(u"MultiRemCounter")
        self.MultiRemCounter.setGeometry(QRect(80, 50, 42, 22))
        self.MultiRemCounter.setCursor(QCursor(Qt.ArrowCursor))
        self.MultiRemCounter.setWrapping(False)
        self.MultiRemCounter.setFrame(True)
        self.MultiRemCounter.setAlignment(Qt.AlignCenter)
        self.MultiRemCounter.setKeyboardTracking(True)
        self.MultiRemCounter.setMinimum(1)
        self.tabWidget.addTab(self.HA, "")
        self.ET = QWidget()
        self.ET.setObjectName(u"ET")
        self.tabWidget.addTab(self.ET, "")
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(0, 270, 361, 111))
        font3 = QFont()
        font3.setFamily(u"Fixedsys")
        font3.setPointSize(4)
        font3.setBold(False)
        font3.setWeight(50)
        self.plainTextEdit.setFont(font3)
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(1, 86, 0);\n"
"\n"
"color: rgb(4, 255, 0);")
        self.plainTextEdit.setTabChangesFocus(False)
        self.plainTextEdit.setUndoRedoEnabled(False)
        self.plainTextEdit.setLineWrapMode(QPlainTextEdit.WidgetWidth)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setOverwriteMode(False)
        self.plainTextEdit.setBackgroundVisible(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Version_Text.setText(QCoreApplication.translate("MainWindow", u"Ver 2.0", None))
        self.OpenGamesBtn.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0627\u0632\u06a9\u0631\u062f\u0646 \u0628\u0627\u0632\u06cc \u0647\u0627", None))
        self.SteamDBCheck.setText(QCoreApplication.translate("MainWindow", u"SteamDB", None))
        self.VarsCheck.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0627\u0632 \u06a9\u0631\u062f\u0646 \u0645\u062a\u063a\u06cc\u0631 \u0647\u0627", None))
        self.G_name_label.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u0628\u0627\u0632\u06cc", None))
        self.OpenGame_SingleBtn.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0627\u0632 \u06a9\u0631\u062f\u0646 \u0628\u0627\u0632\u06cc", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.OG), QCoreApplication.translate("MainWindow", u"\u0628\u0627\u0632 \u06a9\u0631\u062f\u0646 \u0628\u0627\u0632\u06cc \u0647\u0627", None))
        self.RemoveDiscBtn.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0630\u0641 \u06a9\u0627\u0645\u0644 \u062a\u062e\u0641\u06cc\u0641", None))
        self.G_name_label_2.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u0628\u0627\u0632\u06cc", None))
        self.RemoveDisc_SingleBtn.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0630\u0641 \u062a\u062e\u0641\u06cc\u0641 \u0628\u0627\u0632\u06cc", None))
        self.OnScreenRemCheck.setText(QCoreApplication.translate("MainWindow", u"OnScreen", None))
        self.MultiRemCheck.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0630\u0641 \u06af\u0631\u0648\u0647\u06cc", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.HA), QCoreApplication.translate("MainWindow", u"\u062d\u0630\u0641 \u062a\u062e\u0641\u06cc\u0641", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ET), QCoreApplication.translate("MainWindow", u"\u0627\u0639\u0645\u0627\u0644 \u062a\u062e\u0641\u06cc\u0641", None))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Program Logs.", None))
    # retranslateUi

