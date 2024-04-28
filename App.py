import sys
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *
import main
import threading


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        # Connect the button click to a function
        self.ui.RemoveDiscBtn.clicked.connect(main.RemoveAllDiscount)
        self.ui.OpenGamesBtn.clicked.connect(self.OpenGamesFullFunc)
        self.ui.OpenGame_SingleBtn.clicked.connect(self.OpenSingleGameinside)

    def OpenGamesFullFunc(self, steamdbcheck=False, variablecheck=False):
        main.FullOpenAllGames(self.ui.SteamDBCheck.isChecked(), self.ui.VarsCheck.isChecked())

    def OpenSingleGameinside(self):
        main.FullOpenSingleGames(self.ui.SteamDBCheck.isChecked(), self.ui.VarsCheck.isChecked(),
                                 self.ui.LinkForOpen_Input.toPlainText())


def mainstart():
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    mainstart()
