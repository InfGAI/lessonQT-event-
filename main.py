import sys

from itertools import combinations
from PyQt5 import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPainter, QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.dots = list()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Координаты')

        self.coords = QLabel(self)
        self.coords.setText("Координаты: None, None")
        self.coords.move(30, 30)

    def paintEvent(self, event) -> None:
        qp = QPainter()
        qp.begin(self) #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
        if len(self.dots) >= 2:
            for i in range(0, len(self.dots), 2):
                x1, y1, x2, y2 = *self.dots[i], *self.dots[i + 1]
                qp.drawLine(x1, y1, x2, y2)
        qp.end()

    def mousePressEvent(self, event) -> None:
        X, Y = event.x(), event.y()
        self.dots.append((X, Y))

    def mouseReleaseEvent(self, event) -> None:
        X, Y = event.x(), event.y()
        self.dots.append((X, Y))
        self.repaint()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())