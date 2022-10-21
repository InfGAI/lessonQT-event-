import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.circleSize = 0
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Координаты')

        self.coords = QLabel(self)
        self.coords.setText("Координаты: None, None")
        self.coords.move(30, 30)

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
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())