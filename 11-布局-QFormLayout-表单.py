from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QFormLayout,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
)
import sys


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("表单")
        # 不能改变大小
        self.setFixedSize(300, 150)
        container = QVBoxLayout()

        form_layout = QFormLayout()

        edit = QLineEdit(self)
        edit.setPlaceholderText("请输入账号")
        form_layout.addRow("账号", edit)

        edit1 = QLineEdit(self)
        edit1.setPlaceholderText("请输入密码")
        form_layout.addRow("密码:", edit1)

        container.addLayout(form_layout)

        login_btn = QPushButton("登录")
        login_btn.setFixedSize(100, 30)
        container.addWidget(login_btn, alignment=Qt.AlignRight)

        self.setLayout(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec()
