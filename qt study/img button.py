import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QAbstractButton
from PyQt5.QtCore import QSize

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
        return QSize(65, 100)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    layout = QHBoxLayout(window)

    button = PicButton(QPixmap("../freaking math/img/true.png"), QPixmap("../freaking math/img/true_select.png"), QPixmap("../freaking math/img/true_select.png"))
    layout.addWidget(button)

    window.show()
    sys.exit(app.exec_())

