import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import  *

import freakingmath
import random, math

WIDTH = 280
HEIGHT = 500
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 100
PADDING = 30
status_bar_height = -1

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.board = Board(self, self.shuffle_background)
        self.setCentralWidget(self.board)

        
        self.board.start()
        screen = QDesktopWidget().screenGeometry()
        self.setGeometry((screen.width() - WIDTH) / 2, (screen.height() - HEIGHT) / 2, WIDTH, HEIGHT)
        self.setWindowTitle('Freaking Math')
        self.show()

    def shuffle_background(self):
        pal = QPalette()
        role = QPalette.Background
        self.random_colors = ["#03a9f4", "#00bcd4", "#673ab7", "#e91e63", "#f44336", "#009688"]
        pal.setColor(role, QColor(random.choice(self.random_colors)))
        self.setPalette(pal)

class Board(QWidget):
    msg2Statusbar = pyqtSignal(str)
    def __init__(self, parent, shuffle_background):
        super().__init__(parent)
        self.initData()
        self.initBoard()
        self.shuffle_background = shuffle_background
        # TODO: using keyboard to select True/False

    def initBoard(self):
##        self.score = 0
        
        # Initialize buttons
        trueBtnX = PADDING
        trueBtnY = HEIGHT - PADDING - BUTTON_HEIGHT
        
        falseBtnX = WIDTH  - PADDING - BUTTON_WIDTH
        falseBtnY = trueBtnY
        
        self.trueBtn = QPushButton("", self)
        self.trueBtn.setGeometry(trueBtnX, trueBtnY, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.trueBtn.setIcon(QIcon(".//img/true.png"))
        self.trueBtn.clicked.connect(self.handleCorrect)
        self.trueBtn.setIconSize(QSize(BUTTON_WIDTH, BUTTON_HEIGHT))

        self.falseBtn = QPushButton("", self)
        self.falseBtn.setGeometry(falseBtnX, falseBtnY, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.falseBtn.setIcon(QIcon(".//img/false.png"))
        self.falseBtn.setIconSize(QSize(BUTTON_WIDTH, BUTTON_HEIGHT))
        self.falseBtn.clicked.connect(self.handleWrong)

        self.correctSound = QSound(".//sound/score.wav")
        self.incorrectSound = QSound(".//sound/gameover.wav")

    def initData(self):
        self.question = ""
        self.score = 0

    def start(self):
        self.msg2Statusbar.emit(str(self.score))
        self.shuffle_background()
        self.getRandomMathProblem()
        # self.timer.start(Board.Speed, self)
        # self.renderNewQuestion()

    def getRandomNum(self):
        min = 1
        max = 10
        randomNum = random.random() * (max - min) + min
        return math.floor(randomNum)

    def getRandomAnswer(self):
        printed_answer = random.random() * (1 + 10) + 1
        return math.floor(printed_answer)

    def getRandomMathProblem(self):
        # self.num1 = self.getRandomNum()
        # self.num2 = self.getRandomNum()
        # self.answer = self.num1 + self.num2

        [self.num1, self.num2, self.sign, self.answer] =  freakingmath.generate_quiz()

        # TODO: need to rename properly genAnswer()

        # if (self.genAnswer() == 0) or (self.genAnswer() == 2):
        #     self.printed_answer = self.answer + 1
        # else:
        #     self.printed_answer = self.answer

##        self.question = ("%s + %d \n= %s"
##                     % (self.num1, self.num2, self.answer))
        if self.sign == "/":
            self.question = "{0} {1} {2} \n= {3:.2f}".format(self.num1, self.sign, self.num2, self.answer)
        else:
            self.question = "{0} {1} {2} \n= {3}".format(self.num1, self.sign, self.num2, self.answer)

        print(self.question)

    # def genAnswer(self):
    #     min = 0
    #     max = 3
    #     randomNum = random.random() * (max - min) + min
    #     return math.floor(randomNum)

    def increaseScore(self):
        self.score += 1
        # self.msg2Statusbar.emit(str(self.score))

    def resetScore(self):
        self.score = 0
        # self.msg2Statusbar.emit(str(self.score))
        # self.msg2Statusbar.emit(str("You Wrong! Reset Scrore."))

    
        
    def handleCorrect(self):
        if freakingmath.check_answer(self.num1, self.num2, self.sign, self.answer, True):
            self.increaseScore()
            self.correctSound.play()
        else:
            self.resetScore()
            self.incorrectSound.play()
        self.getRandomMathProblem()
        self.shuffle_background()
        self.repaint()

    def handleWrong(self):
        if freakingmath.check_answer(self.num1, self.num2, self.sign, self.answer, False):
            self.increaseScore()
            self.correctSound.play()
        else:
            self.resetScore()
            self.incorrectSound.play()
        self.getRandomMathProblem()
        self.shuffle_background()
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()

    def drawText(self, event, qp):
        # Draw question
        qp.setPen(QColor("#fafafa"))
        qp.setFont(QFont('Roboto', 48, QFont.Bold))
        qp.drawText(QRect(0, 0, WIDTH, HEIGHT), Qt.AlignCenter, self.question)

        # Draw score
        qp.setPen(QColor("#fafafa"))
        qp.setFont(QFont('Roboto', 20, QFont.Bold))
        qp.drawText(QRect(0, 0, WIDTH, HEIGHT), Qt.AlignTop | Qt.AlignRight, str(self.score)) #Bit mask

        # TODO: Add Timer

    # def renderNewQuestion(self):
    #     self.getRandomMathProblem()
    #     self.repaint()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
