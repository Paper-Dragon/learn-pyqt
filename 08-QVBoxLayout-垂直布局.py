import sys

from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import (
    QApplication,
    QDesktopWidget,
    QPushButton,
    QLineEdit,
    QLabel,
    QWidget,
    QVBoxLayout,
)


class MyWindow(QWidget):
    def __init__(self):
        # 切记一定要记得调用父类的__init__()方法，因为它有很对对UI空间的初始化操作
        super().__init__()
        # 设置大小
        self.resize(1024, 768)
        # 设置标题
        self.setWindowTitle("垂直布局")

        # 垂直布局
        layout = QVBoxLayout()
        # 作用是在布局器中增加一个伸缩量，里面的参数表示QSpacerItem的个数，默认值为零
        # 会将你放在layout中的空间压缩成默认的大小
        # 下面的笔试1：1：1：2
        # layout.addStretch(1)

        # 按钮1
        btn1 = QPushButton("按钮1")
        # 添加到布局器中
        # layout.addWidget(btn1, Qt.AlignmentFlag.AlignTop)
        layout.addWidget(btn1)
        # layout.addStretch(1)

        # 按钮2
        btn2 = QPushButton("按钮2")
        # 添加到布局器
        layout.addWidget(btn2)
        # layout.addStretch(1)

        # 按钮3
        btn3 = QPushButton("按钮3")
        # 添加到布局器
        layout.addWidget(btn3)
        layout.addStretch(2)

        self.setLayout(layout)

    def get_window_size(self):
        """
        获取窗口大小
        :return:  width, height
        """
        old_x, old_y, width, height = self.frameGeometry().getRect()
        return width, height

    @staticmethod
    def get_center_point():
        center_point = QDesktopWidget().availableGeometry().center()
        return center_point.x(), center_point.y()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()

    w.show()
    app.exec_()
