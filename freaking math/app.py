import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
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
    def __init__(self, parent):
        super().__init__(parent)

        self.initBoard()

    def initBoard(self):
        self.timer = QBasicTimer()
        self.isStarted = False
        self.setAutoFillBackground(False)
        # self.clearBoard()
        self.score = 0

        # self.startBtn = QPushButton("Start", self)
        # self.startBtn.move(200, 10)
        # self.startBtn.clicked.connect(self.renderNewQuestion)

        self.button = PicButton(QPixmap("./img/true.png"), QPixmap("./img/true_select.png"), QPixmap("./img/true_select.png"))

        self.trueBtn = QPushButton("True", self)
        self.trueBtn.move(50, 150)
        self.trueBtn.clicked.connect(self.handleCorrect)

        self.falseBtn = QPushButton("False", self)
        self.falseBtn.move(150, 150)
        self.falseBtn.clicked.connect(self.handleWrong)


    def start(self):
        self.msg2Statusbar.emit(str(self.score))
        # self.timer.start(Board.Speed, self)
        self.renderNewQuestion()

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
            self.printed_answer = self.answer + 1
        else:
            self.printed_answer = self.answer

        self.text = ("%s + %d \n= %s"
                     % (self.num1, self.num2, self.printed_answer))

        print("%s + %d \n= %s"
                     % (self.num1, self.num2, self.printed_answer))

    def genAnswer(self):
        min = 0
        max = 3
        randomNum = random.random() * (max - min) + min
        return math.floor(randomNum)

    def increaseScore(self):
        self.score += 1
        self.msg2Statusbar.emit(str(self.score))
        self.renderNewQuestion()

    def resetScore(self):
        self.score = 0
        self.msg2Statusbar.emit(str(self.score))

    def handleCorrect(self):
        if self.printed_answer == self.answer:
            self.increaseScore()
        else:
            self.resetScore()
        # self.renderNewQuestion()

    def handleWrong(self):
        if self.printed_answer != self.answer:
            self.increaseScore()
        else:
            self.resetScore()
        # self.renderNewQuestion()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()

    def drawText(self, event, qp):
        qp.setPen(QColor(100, 100, 100))
        qp.setFont(QFont('Relay', 16))
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)

    def renderNewQuestion(self):
        self.getRandomMathProblem()
        self.repaint()

class PicButton(QAbstractButton):
    def __init__(self, pixmap, pixmap_hover, pixmap_pressed, parent=None):
        super(PicButton, self).__init__(parent)
        self.pixmap = pixmap
        self.pixmap_hover = pixmap_hover
        self.pixmap_pressed = pixmap_pressed

        self.pressed.connect(self.update)
        self.released.connect(self.update)

    def paintEvent(self, event):
        pix = self.pixmap_hover if self.underMouse() else self.pixmap
        if self.isDown():
            pix = self.pixmap_pressed

        painter = QPainter(self)
        painter.drawPixmap(event.rect(), pix)

    def enterEvent(self, event):
        self.update()

    def leaveEvent(self, event):
        self.update()

    def sizeHint(self):
        return QSize(20, 20)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    # app.processEvents()
    sys.exit(app.exec_())
