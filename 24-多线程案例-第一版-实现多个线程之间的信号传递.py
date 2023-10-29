import json
import sys
import time

from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class LoginThread(QThread):
    start_login_signal = pyqtSignal(str)

    def __init__(self, login_status_signal):
        self.login_status_signal = login_status_signal
        super().__init__()

    def login_by_requests(self, user_login_json):
        time.sleep(5)
        print(user_login_json)

    def run(self) -> None:
        i = 0
        while True:
            i += 1
            print(f"子线程正在运行。。。{i}")
            time.sleep(1)


class MyWindow(QWidget):
    login_status_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()

    def login(self):
        """登录按钮的槽函数"""
        user_name = self.user_name_qwidget.text()
        password = self.password_qwidget.text()
        # time.sleep(3)
        self.login_thread.start_login_signal.emit(
            json.dumps({"username": user_name, "password": password})
        )

        # if user_name == "admin" and password == "123456":
        #     time.sleep(3)
        #     self.textBrowser.setText("欢迎%s" % user_name)
        #     self.textBrowser.repaint()
        #
        # else:
        #     self.textBrowser.setText("用户名或密码错误....请重试")
        #     self.textBrowser.repaint()

    def login_status(self, status):
        print(f"status -> {status}")
        status_dicts = json.loads(status)
        self.textBrowser.setText(status_dicts.get("errmsg"))
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

        self.login_thread = LoginThread(self.login_status_signal)
        self.login_thread.start_login_signal.connect(
            self.login_thread.login_by_requests
        )
        self.login_thread.start()

        self.login_status_signal.connect(self.login_status)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.ui.show()
    app.exec()
