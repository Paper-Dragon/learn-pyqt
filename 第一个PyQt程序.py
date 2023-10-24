import sys

from PyQt5.QtGui import QIcon
from PyQt5 import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QDesktopWidget,
)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()

    # 设置窗口标题
    w.setWindowTitle("QT写的程序")

    w.resize(300, 300)

    # w.setWindowFlags(Qt.Qt.FramelessWindowHint)  # 去掉标题栏的代码

    w.setWindowIcon(QIcon('icon.ico'))
    # 将窗口设置在屏幕的左上角
    # w.move(0, 0)

    # 调整窗口在屏幕中央显示
    center_pointer = QDesktopWidget().availableGeometry().center()
    x = center_pointer.x()
    y = center_pointer.y()
    # w.move(x, y)
    # w.move(x-150, y-150)
    print(w.frameGeometry())
    print(w.frameGeometry().getRect())
    print(type(w.frameGeometry().getRect()))
    old_x, old_y, width, height = w.frameGeometry().getRect()
    w.move(int(x - width / 2), int(y - height / 2))

    # # 下面创建一个Label，然后调用方法指定父类
    # label = QLabel("账号: ", w)
    # # 设置父对象
    # label.setParent(w)

    # 下面创建一个Label（纯文本），在创建的时候指定了父对象
    label = QLabel("账号: ", w)

    # 显示位置与大小 ： x, y , w, h0
    label.setGeometry(20, 20, 30, 20)

    edit = QLineEdit(w)
    edit.setPlaceholderText("请输入账号")
    edit.setGeometry(55, 20, 200, 20)

    btn = QPushButton("注册", w)
    btn.setGeometry(50, 80, 70, 30)

    # 展示窗口
    w.show()

    # 程序进入循环等待状态
    app.exec()
