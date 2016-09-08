import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAbstractButton, QWidget, QHBoxLayout, QLabel, QLineEdit
from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtCore import QSize
from threading import Timer
import math, random
from socket import *

g = True
score = 0
sec = 0

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton("True", self)
        btn1.move(75, 450)

        btn2 = QPushButton("False", self)
        btn2.move(225, 450)

        self.setGeometry(500, 100, 400, 600)
        self.setWindowTitle('Freaking Math              made by Pt')
        self.show()

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

    def getRandomNum(self):
        min = 1
        max = 10
        randomNum = random.random() * (max - min) + min
        return math.floor(randomNum)


    def randomNumber(self):
        self.random = self.getRandomNum()
        self.first = self.getRandomNum()
        self.second = self.getRandomNum()
        self.answer = self.first + self.second
        if (self.random == 0):
            g = True
        else:
            g = False


    def count(self):
        global score
        self.score = score + 1

    def resetMath(self):
        global score
        self.score = 0

    def checkTrue(self):
        # clearTime()
        if (g == True):
            self.count()
            self.randomNumber()
        else:
            self.resetMath()


    def checkFalse(self):
        # clearTime()
        if (self.g == False):
            self.count()
            self.randomNumber()
        else:
            self.resetMath()

    def start(self):
        # clearTime()
        self.g = True
        self.randomNumber()
        self.score = 0

    # def creatTime():
    #     timeCount = Timer(1000, resetMath()).start()
    #
    # def clearTime():
    #     clearInterval(timeCount)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())