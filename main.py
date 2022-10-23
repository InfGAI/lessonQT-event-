import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QInputDialog, QPushButton, QDialog


class ExceptionHandler(QtCore.QObject):
    errorSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(ExceptionHandler, self).__init__()

    def handler(self, exctype, value, traceback):
        self.errorSignal.emit()
        sys._excepthook(exctype, value, traceback)

class Choice(QWidget):
    def __init__(self):
        super().__init__()
        self.ch_win = None
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Координаты')

        self.coords = QLabel(self)
        self.coords.setText("Координаты: None, None")
        self.coords.move(30, 30)

    def mouseMoveEvent(self, event):
        self.coords.setText(f"Координаты: {event.x()}, {event.y()}")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_C:
            self.ch_win = ChWin()

            self.ch_win.show()

        # code

class ChWin(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('important choice')
        self.yes = QPushButton('yes', self)
        self.yes.move(20, 20)
        self.yes.resize(70, 20)
        self.no = QPushButton('no', self)
        self.no.move(100, 20)
        self.no.resize(70, 20)

if __name__ == '__main__':
    exceptionHandler = ExceptionHandler()
    sys._excepthook = sys.excepthook
    sys.excepthook = exceptionHandler.handler
    app = QApplication(sys.argv)
    ch = Choice()
    ch.show()
    sys.exit(app.exec())

