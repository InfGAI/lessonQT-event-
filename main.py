# При нажатии кнопки F - открывается окно настройки шрифта, шрифт применяется к надписи we are all lazy
# При нажатии правой кнопки мыши рисуется круг
import sys
import traceback
from PyQt5.QtCore import Qt # Qt нужно импортить именно из QtCore! не просто из PyQt5 как предлагает контескстное меню
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton,
                             QSizePolicy, QLabel, QFontDialog, QApplication)

# Вставка для обработки исключений, чтобы выводились подробные ошибки, а не просто код ошибки
def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error catched!:")
    print("error message:\n", tb)
    QApplication.quit()


sys.excepthook = excepthook


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.dots = (10,10)
        self.circles = [(self.dots[0],self.dots[1], 50, 50)]
        self.text = QLabel('we are all lazy', self)
        self.text.move(170, 40)

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Координаты')
        self.coords = QLabel(self)
        self.coords.setText("Координаты: None, None")
        self.coords.move(30, 30)

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton: # обработка правой кнопки  мышки
            self.coords.setText(f"Координаты: {event.x()}, {event.y()}")
            X, Y = event.x(), event.y() # координаты положения курсора
            self.dots = (X, Y)
            self.circles.append((self.dots[0],self.dots[1], 50, 50))
            self.repaint() # метод, вызывающий перерисовку изображения(то, что указано в paintEvent)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        for i in self.circles:
            qp.drawEllipse(i[0], i[1], i[2], i[3]) # Отрисовка кругов
        qp.end()


    def showDialog(self):
        font, ok = QFontDialog.getFont()  # диалоговое окно изменения шрифта
        if ok:
            self.text.setFont(font)

    def keyPressEvent(self, event) -> None:
        if event.key() == Qt.Key_F: # обработки нажатия P
            self.showDialog()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
