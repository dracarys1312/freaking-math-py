import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui import QImage
import urllib.request
from PyQt5 import QtGui


class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # hbox = QHBoxLayout(self)
        # url = 'https://raw.githubusercontent.com/evertheylen/freakingmath-hack/master/img/true.png'
        # data = urllib.request.urlopen(url).read()
        #
        # image = QImage()
        # image.loadFromData(data)
        #
        # lbl = QLabel(self)
        # lbl.setPixmap(QtGui.QPixmap(image))
        #
        # hbox.addWidget(lbl)
        # self.setLayout(hbox)

        btn1 = QPushButton("True", self)
        btn1.move(75, 450)

        btn2 = QPushButton("False", self)
        btn2.move(225, 450)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(500, 100, 400, 600)
        self.setWindowTitle('Freaking Math              made by Pt')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()

    def drawRectangles(self, qp):
        col = QColor(0, 0, 0)
        col.setNamedColor('#f3f3f3')
        qp.setPen(col)

        qp.setBrush(QColor(46, 204, 113))
        qp.drawRect(0, 0, 400, 600)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())