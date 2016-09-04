import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui import QImage
import urllib.request
from PyQt5 import QtGui

class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)

        url = 'https://raw.githubusercontent.com/evertheylen/freakingmath-hack/master/img/true.png'
        data = urllib.request.urlopen(url).read()

        image = QImage()
        image.loadFromData(data)

        lbl = QLabel("True")
        lbl.setPixmap(QtGui.QPixmap(image))

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.show()

def main():
    import sys

    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

