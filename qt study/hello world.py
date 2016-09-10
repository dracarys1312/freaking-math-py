import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import random, math

class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.board = Board(self)
        self.setCentralWidget(self.board)

        self.statusbar = self.statusBar()
        self.board.msg2Statusbar[str].connect(self.statusbar.showMessage)

        self.board.start()

        self.setGeometry(550, 300, 280, 200)
        self.center()
        self.setWindowTitle('Freaking Math')
        self.show()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

class Board(QWidget):
    msg2Statusbar = pyqtSignal(str)

    # setAutoFillBackground(self)
    def __init__(self, parent):
        super().__init__(parent)

        self.initBoard()

    def initBoard(self):
        self.score = 0
        self.startBtn = QPushButton("Start", self)
        self.startBtn.move(200, 10)
        self.startBtn.clicked.connect(self.getRandomMathProblem)

        self.trueBtn = QPushButton("True", self)
        self.trueBtn.move(50, 150)
        self.trueBtn.clicked.connect(self.handleCorrect)

        self.falseBtn = QPushButton("False", self)
        self.falseBtn.move(150, 150)
        self.falseBtn.clicked.connect(self.handleWrong)

        self.b = QLabel('', self)
        self.b.move(125, 80)

    def start(self):
        self.isStarted = True
        self.msg2Statusbar.emit(str(self.score))
        self.getRandomMathProblem()

    def getRandomNum(self):
        min = 1
        max = 10
        randomNum = random.random() * (max - min) + min
        return math.floor(randomNum)

    def getRandomAnswer(self):
        printed_answer = random.random() * (1 + 10) + 1
        return math.floor(printed_answer)

    def getRandomMathProblem(self):
        self.num1 = self.getRandomNum()
        self.num2 = self.getRandomNum()
        self.answer = self.num1 + self.num2
        # TODO: need to rename properly genAnswer()
        if (self.genAnswer() == 0) or (self.genAnswer() == 2):
            self.printed_answer = self.getRandomAnswer()
        else:
            self.printed_answer = self.answer
        self.b.setText("%d + %d \n = %d" % (self.num1, self.num2, self.printed_answer))
        # self.b.clear()
        print("%d + %d \n = %d" % (self.num1, self.num2, self.printed_answer))
    def genAnswer(self):
        min = 0
        max = 3
        randomNum = random.random() * (max - min) + min
        return math.floor(randomNum)

    def increaseScore(self):
        self.score += 1
        self.msg2Statusbar.emit(str(self.score))
        # self.b.clear()
        self.getRandomMathProblem()

    def resetScore(self):
        self.score = 0
        self.msg2Statusbar.emit(str(self.score))

    def handleCorrect(self):
        if self.printed_answer == self.answer:
            self.increaseScore()
        else:
            self.resetScore()
        self.getRandomMathProblem()


    def handleWrong(self):
        if self.printed_answer != self.answer:
            self.increaseScore()
            # self.getRandomMathProblem()
        else:
            self.resetScore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
