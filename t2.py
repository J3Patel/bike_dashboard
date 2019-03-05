import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def setColor(self, layout):
        layout.setAutoFillBackground(True)
        p = layout.palette()
        p.setColor(layout.backgroundRole(), QColor(0x202020).darker())
        p.setColor(layout.foregroundRole(), QColor(0xFFFFFF))
        layout.setPalette(p)

    def addSpeedometer(self, layout):
        self.speedLbl = QLabel('75', self)
        font = QtGui.QFont("Dodger Condensed Italic", 100, 1)
        self.setColor(self.speedLbl)
        self.speedLbl.setFont(font)
        layout.addWidget(self.speedLbl)

    def addCloseBtn(self, layout):
        closeBtn = QPushButton("close")
        layout.addWidget(closeBtn)
        closeBtn.pressed.connect(lambda: self.closeBtnAction())

    def setupMainGrid(self):
        mainGridLayout = QVBoxLayout()
        mainGridLayout.setSpacing(0)
        return mainGridLayout

    def setupTopBoxLayout(self, layout):
        thbl = QHBoxLayout()
        layout.addLayout(thbl, 2)
        self.addSpeedometer(thbl)
        self.setupGA(thbl)
        thbl.setSpacing(0)
       # thbl.setContentsMargins(0,0,0,0)
        return thbl

    def setupMapView(self, layout):
        thbl = QHBoxLayout()
        self.webView = QWebView()
        self.webView.load(QUrl("https://maps.google.com"))
        thbl.addWidget(self.webView)
        layout.addLayout(thbl, 5)

    def setupGA(self, layout):
        micBtn = QPushButton()
        micBtn.setIcon(QtGui.QIcon("./images/mic2.png"))
        micBtn.setIconSize(QtCore.QSize(140,140))
        self.setColor(micBtn)
        layout.addWidget(micBtn)

    def initUI(self):
        mainGridLayout = self.setupMainGrid()
        topHBoxView = self.setupTopBoxLayout(mainGridLayout)
        mapView = self.setupMapView(mainGridLayout)
        mainGridLayout.setContentsMargins(0,0,0,0)
        self.setLayout(mainGridLayout)

        self.setWindowTitle('Absolute')
        self.showFullScreen()

#Actions
    def closeBtnAction(self):
        self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('/home/pi/samurai/sam/font/Dodgv2ci.ttf')
    ex = Example()
    sys.exit(app.exec_())
