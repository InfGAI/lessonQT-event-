import sys

from PyQt5 import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from random import randrange
from PIL import Image, ImageDraw


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Координаты')

        self.coords = QLabel(self)
        self.coords.setText("Координаты: None, None")
        self.coords.move(30, 30)
        self.label = QLabel(self)
        self.label.resize(400, 400)
        self.label.move(0, 50)

    def mouseMoveEvent(self, event):
        self.coords.setText(f"Координаты: {event.x()}, {event.y()}")

    def keyPressEvent(self, event):
        print(int(event.key()))
        if int(event.key()) in [49, 50, 51]:
            # print(int(event.key()))
            self.count = int(event.key()) % 48
            self.make_img(self.count)
        # code

    def make_img(self, count):

        main_im = Image.new("RGB", (400, 400), (255, 255, 255))

        for i in range(count):
            side = randrange(20, 0)
            im = Image.new("RGB", (side, side), (255, 0, 0))
            main_im.paste(im, (randrange(0, 300), randrange(0, 300)))
            

        main_im.save("im.png")

        self.pix = QPixmap("im.png")
        self.label.setPixmap(self.pix)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
