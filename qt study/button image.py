import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class AllGreen(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.w = QWidget(self)
        self.w.setFixedSize(100, 100)

        palette = self.palette()
        role = self.backgroundRole()
        palette.setColor(role, QColor('green'))
        self.setPalette(palette)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AllGreen()
    ex.setGeometry(300, 300, 250, 150)
    ex.show()
    sys.exit(app.exec_())