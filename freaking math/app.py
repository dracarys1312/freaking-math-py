#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we draw text in Russian azbuka.

author: Jan Bodnar
website: zetcode.com
last edited: September 2015
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt
import random
import math

scrore = 0

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def getRandomNum(self):
        min = 1
        max = 10
        randomNum = random.random() * (max - min) + min
        return math.floor(randomNum)

    def initUI(self):
        # self.text = ("%s + %d \n= %s" % (self.getRandomNum(), self.getRandomNum(), self.getRandomNum()))
        self.num1 = self.getRandomNum()
        self.num2 = self.getRandomNum()
        self.randomNum = self.getRandomNum()
        self.answer = self.num1 + self.num2
        self.text = ("%s + %d \n= %s" % (self.num1, self.num2, self.randomNum))

        self.setGeometry(550, 300, 280, 200)

        startbtn = QPushButton("Start", self)
        startbtn.move(200, 10)

        truebtn = QPushButton("True", self)
        truebtn.move(50, 150)

        falsebtn = QPushButton("False", self)
        falsebtn.move(150, 150)

        # truebtn.clicked.connect(self.status)
        # falsebtn.clicked.connect(self.status)

        # self.statusBar()

        self.setWindowTitle('Freaking Math')
        self.show()

    def status(self):
        sender = self.sender()
        if self.randomNum == self.answer:

            self.statusBar().showMessage(sender.text() + ' was right')
        else:
            self.statusBar().showMessage(sender.text() + ' was false')

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()

    def drawText(self, event, qp):
        # qp.setPen(QColor(168, 34, 3))
        # qp.setFont(QFont('Roboto', 14))
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)

    # def handleAnswer(self):
    #     sender = self.sender()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())