import os
import sys
import time

from PyQt5 import uic
from PyQt5.Qt import QApplication, QWidget, QThread


class MyThread(QThread):
    def __init__(self):
        super().__init__()

    def run(self) -> None:
        for i in range(10):
            print(f"线程{i}启动！！")
            time.sleep(1)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi(os.path.join(os.path.dirname(__file__), "muti_thread.ui"))
        print(self.ui.__dict__)
        lineedit = self.ui.lineEdit
        btn1 = self.ui.pushButton
        btn2 = self.ui.pushButton_2
        btn1.clicked.connect(self.btn1_clicked)
        btn2.clicked.connect(self.btn2_clicked)

    def btn1_clicked(self):
        for i in range(10):
            self.my_thread = MyThread()
            self.my_thread.start()

    def btn2_clicked(self):
        self.my_thread = MyThread()  # 创建线程
        self.my_thread.start()  # 开始线程


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.ui.show()
    app.exec()