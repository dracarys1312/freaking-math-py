import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAbstractButton, QWidget, QHBoxLayout, QLabel, QLineEdit


def Ui_ImageDialog():
    app = QApplication(sys.argv)
    w = QWidget()
    b = QLabel(w)
    b.setText("Hello World!")
    w.setGeometry(100, 100, 200, 50)
    b.move(50, 20)
    w.setWindowTitle('PyQt')
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()