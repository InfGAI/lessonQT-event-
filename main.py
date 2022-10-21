import sys

<<<<<<< HEAD
from itertools import combinations
from PyQt5 import Qt
=======
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
>>>>>>> 245cddf911e0fdaa8f0e18114d49998eccde9abc
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPainter, QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.circleSize = 0
        self.initUI()
        self.dots = list()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Координаты')

        self.coords = QLabel(self)
        self.coords.setText("Координаты: None, None")
        self.coords.move(30, 30)

<<<<<<< HEAD
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


=======
    def keyPressEvent(self, event):
        if int(event.modifiers()) == (Qt.AltModifier + Qt.ShiftModifier):
            if event.key == Qt.key_Q:
                pass
        # Adding and removing circles
        if event.key() == Qt.Key_Z:
            self.circleSize += 1
            self.update()
        if event.key() == Qt.Key_X:
            self.circleSize -= 1
            if self.circleSize < 0:
                self.circleSize = 0
            self.update()


    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawCircle(qp)
        qp.end()

    def drawCircle(self, qp):
        qp.setBrush(Qt.black)
        qp.drawEllipse(150 - self.circleSize // 2, 150 - self.circleSize // 2, self.circleSize, self.circleSize)
>>>>>>> 245cddf911e0fdaa8f0e18114d49998eccde9abc

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())