import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Example(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.label = QLabel(self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        self._text = 'this is a test'
        self._index = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.handleTimer)
        self.timer.start(200)

    def handleTimer(self):
        self._index += 1
        self.label.setText(self._text[:self._index])
        if self._index > len(self._text):
            self.timer.stop()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.setGeometry(300, 300, 250, 150)
    ex.show()
    sys.exit(app.exec_())