import sys

from random import randint as rint
from PyQt5 import Qt
from PyQt5 import QtCore
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Координаты')

        self.coords = QLabel(self)
        self.coords.setText("Координаты: None, None")
        self.coords.move(30, 30)

    def mouseMoveEvent(self, event):
        self.coords.setText(f"Координаты: {event.x()}, {event.y()}")

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            palette = QPalette()
            palette.setColor(QPalette.Background, QColor(rint(0, 255), rint(0, 255), rint(0, 255)))
            self.setPalette(palette)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())