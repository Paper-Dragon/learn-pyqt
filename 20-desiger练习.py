import sys
import time

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def login(self):
        """登录按钮的槽函数"""
        user_name = self.user_name_qwidget.text()
        password = self.password_qwidget.text()
        time.sleep(3)
        if user_name == "admin" and password == "123456":
            self.textBrowser.setText("欢迎%s" % user_name)
            self.textBrowser.repaint()

        else:
            self.textBrowser.setText("用户名或密码错误....请重试")
            self.textBrowser.repaint()

    def init_ui(self):
        self.ui = uic.loadUi("./feiqq.ui")
        print(self.ui.__dict__)

        self.user_name_qwidget = self.ui.LineEdit
        self.password_qwidget = self.ui.LineEdit_2
        self.login_btn = self.ui.pushButton
        self.forget_password = self.ui.pushButton_2
        self.textBrowser = self.ui.textBrowser

        self.login_btn.clicked.connect(self.login)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.ui.show()
    app.exec()
