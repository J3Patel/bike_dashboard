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
        p.setColor(layout.backgroundRole(), QColor(0x34495E).darker().darker())
        p.setColor(layout.foregroundRole(), QColor(0xFFFFFF))
        layout.setPalette(p)

    def setFont(self, widget, size):
        font = QtGui.QFont("Dodger Condensed Italic", size, 1)
        widget.setFont(font)

    def setDigitalFont(self, widget, size):
        font = QtGui.QFont("Digital-7 Italic", size, 1)
        widget.setFont(font)

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
        self.addTripMeter(thbl)
        # self.setupIndicatorView(thbl)
        # self.setupGA(thbl)
        self.setupGA(thbl)
        thbl.setSpacing(0)
        return thbl

    def addSpeedometer(self, layout):
        self.speedLbl = QLabel('21', self)
        self.speedLbl.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.setFont(self.speedLbl, 100)
        self.setColor(self.speedLbl)
        layout.addWidget(self.speedLbl, 2)

    def addTripMeter(self, layout):
        vbox = QVBoxLayout()
        layout.addLayout(vbox, 1)

        indicatorV = self.setupIndicatorView(vbox)

        self.totalLb = QLabel('10000', self)
        self.totalLb.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.setColor(self.totalLb)
        self.setDigitalFont(self.totalLb, 20)
        vbox.addWidget(self.totalLb, 1)

        tlb = QHBoxLayout()
        vbox.addLayout(tlb, 0.7)
        tlb.setSpacing(1)

        tripLabel = QLabel('T 1', self)
        tripLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom )
        self.setColor(tripLabel)
        self.setFont(tripLabel, 12)
        tlb.addWidget(tripLabel, 1)

        trip2Label = QLabel('T 2', self)
        trip2Label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom )
        self.setColor(trip2Label)
        self.setFont(trip2Label, 12)
        tlb.addWidget(trip2Label, 1)

        tlvb = QHBoxLayout()
        vbox.addLayout(tlvb, 1)
        tlvb.setSpacing(1)

        self.tripLbl1 = QLabel('50', self)
        self.tripLbl1.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter )
        self.setColor(self.tripLbl1)
        self.setDigitalFont(self.tripLbl1, 20)
        tlvb.addWidget(self.tripLbl1, 1)

        self.tripLbl2 = QLabel('4800', self)
        self.tripLbl2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter )
        self.setColor(self.tripLbl2)
        self.setDigitalFont(self.tripLbl2, 20)
        tlvb.addWidget(self.tripLbl2, 1)

    def startIndicator(self, dir):
        switcher = {
            1: startRIndicator,
            2: startLIndicator,
            3: startNIndicator
        }
        func = switcher.get(dir, lambda: "invalid case")
        func()
    def startRIndicator(self):
        print("started right")

    def startLIndicator(self):
        print("started left")

    def startNIndicator(self):
        print("started Neutral")

    def setupIndicatorView(self, layout):
        iv = QHBoxLayout()
        isize = 50
        lIB = QPushButton()
        lIB.setFlat(True)
        lIB.setIcon(QtGui.QIcon("./images/left_off.png"))
        lIB.setIconSize(QtCore.QSize(isize,isize))
        self.setColor(lIB)
        iv.addWidget(lIB, 1)

        nIB = QPushButton()
        nIB.setFlat(True)
        nIB.setIcon(QtGui.QIcon("./images/neutral_off.png"))
        nIB.setIconSize(QtCore.QSize(isize,isize))
        self.setColor(nIB)
        iv.addWidget(nIB, 1)

        rIB = QPushButton()
        rIB.setFlat(True)
        rIB.setIcon(QtGui.QIcon("./images/right_off.png"))
        rIB.setIconSize(QtCore.QSize(isize,isize))
        self.setColor(rIB)
        iv.addWidget(rIB, 1)

        layout.addLayout(iv, 3)

    def setupGA(self, layout):
        micBtn = QPushButton()
        micBtn.setFlat(True)
        micBtn.setIcon(QtGui.QIcon("./images/mic_on.png"))
        micBtn.setIconSize(QtCore.QSize(140,140))
        self.setColor(micBtn)
        layout.addWidget(micBtn, 1)

    def setupMapView(self, layout):
        thbl = QHBoxLayout()
        self.webView = QWebView()
        self.webView.load(QUrl("https://maps.google.com"))
        thbl.addWidget(self.webView)
        layout.addLayout(thbl, 5)

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
    QtGui.QFontDatabase.addApplicationFont('./font/Dodgv2ci.ttf')
    QtGui.QFontDatabase.addApplicationFont('./font/digital_r.ttf')
    ex = Example()
    sys.exit(app.exec_())
