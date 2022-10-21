import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5 import QtGui, QtCore


class ExceptionHandler(QtCore.QObject):
    errorSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(ExceptionHandler, self).__init__()

    def handler(self, exctype, value, traceback):
        self.errorSignal.emit()
        sys._excepthook(exctype, value, traceback)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.circleSize = 0
        self.initUI()
        self.dots = list()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Координаты')

        self.image = QLabel(self)
        self.image.setPixmap(QPixmap("arrgn.png"))
        self.image.hide()

    def paintEvent(self, event) -> None:
        qp = QPainter()
        qp.begin(self)  # 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
        if len(self.dots) >= 2:
            for i in range(0, len(self.dots), 2):
                x1, y1, x2, y2 = *self.dots[i], *self.dots[i + 1]
                qp.drawLine(x1, y1, x2, y2)
        qp.end()

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.buttons() == Qt.LeftButton:
            self.image.move(event.x(), event.y())

    def mousePressEvent(self, event) -> None:
        x, y = event.x(), event.y()
        self.dots.append((x, y))
        if event.buttons() == Qt.LeftButton:
            self.image.move(x, y)
            self.image.show()

    def mouseReleaseEvent(self, event) -> None:
        x, y = event.x(), event.y()
        self.dots.append((x, y))
        self.repaint()
        if event.button() == Qt.LeftButton:
            self.image.hide()

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


if __name__ == '__main__':
    exceptionHandler = ExceptionHandler()
    sys._excepthook = sys.excepthook
    sys.excepthook = exceptionHandler.handler
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
