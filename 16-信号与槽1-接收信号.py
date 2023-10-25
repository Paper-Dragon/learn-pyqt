import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def clicked_button(self, arg):
        print("clicked!!!!", arg)

    def init_ui(self):
        self.setWindowTitle("发信号")
        self.setFixedSize(300, 200)
        btn = QPushButton("click！！", self)
        btn.setGeometry(100, 100, 80, 30)
        btn.clicked.connect(self.clicked_button)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec()
