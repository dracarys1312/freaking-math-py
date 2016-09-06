import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAbstractButton, QWidget, QHBoxLayout
from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtCore import QSize
from threading import Timer
import math, random
from socket import *

class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
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

g = True
score = 0
sec = 0

def getRandomNum():
    min = 1
    max = 10
    randomNum = random.random() * (max - min) + min
    return math.floor(randomNum)


def randomNumber():
    random = getRandomNum()
    first = getRandomNum()
    second = getRandomNum()
    answer = first + second
    if (random == 0):
        g = True
    else:
        g = False


def count():
    global score
    score = score + 1

def resetMath():
    global score
    score = 0

def checkTrue():
    # clearTime()
    if (g == True):
        count()
        randomNumber()
    else:
        resetMath()


def checkFalse():
    # clearTime()
    if (g == False):
        count()
        randomNumber()
    else:
        resetMath()


def start():
    # clearTime()
    g = True
    randomNumber()
    score = 0

# def creatTime():
#     timeCount = Timer(1000, resetMath()).start()
#
# def clearTime():
#     clearInterval(timeCount)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())