import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("九宫格布局")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec()
