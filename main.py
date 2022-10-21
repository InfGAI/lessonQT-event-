import sys

from PyQt5 import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Координаты')
        self.run_btn = QPushButton(self)
        self.run_btn.setGeometry(100, 100, 100, 100)
        self.run_btn.move(100, 100)
        self.coords = QLabel(self)
        self.coords.setText("Координаты: None, None")
        self.coords.move(30, 30)
        self.last_cords = (0,0)
        self.first = True


    def mouseMoveEvent(self, event):

        x, y = event.x(), event.y()
        print(x)
        if self.first:
            self.last_cords = (x, y)
            self.first = False
        else:
            print()
            xo = self.run_btn.pos().x()
            yo = self.run_btn.pos().y()
            if abs(self.last_cords[0] - xo) > abs(x - xo) and 1 < xo < 400:
                xo += (-self.last_cords[0] + x) + 500
            if abs(self.last_cords[1] - yo) > abs(y - yo) and 1 < yo < 400:
                yo += (-self.last_cords[1] + y) + 500
            print(xo, yo)
            self.run_btn.move(xo % 500, yo % 500)

            self.last_cords = (x, y)


    def keyPressEvent(self, event):
        self.last_cords = (0,0)
        if int(event.modifiers()) == (Qt.AltModifier + Qt.ShiftModifier):
            if event.key() == Qt.Key_Q:
                pass

    def mouseReleaseEvent(self, event):
        self.first = True



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
