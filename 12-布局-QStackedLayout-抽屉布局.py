from PyQt5.QtWidgets import QApplication, QWidget, QStackedLayout, QVBoxLayout, QPushButton, QLabel
import sys


class Window1(QWidget):
    def __init__(self):
        super().__init__()
        QLabel("抽屉1", self)
        self.setStyleSheet("background-color:green;")


class Window2(QWidget):
    def __init__(self):
        super().__init__()
        QLabel("抽屉2", self)
        self.setStyleSheet("background-color:red;")


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.create_stack_layout()
        self.init_ui()

    def btn1_clicked(self):
        self.stacked_layout.setCurrentIndex(0)

    def btn2_clicked(self):
        self.stacked_layout.setCurrentIndex(1)

    def create_stack_layout(self):
        self.stacked_layout = QStackedLayout()
        win1 = Window1()
        win2 = Window2()
        self.stacked_layout.addWidget(win1)
        self.stacked_layout.addWidget(win2)

    def init_ui(self):
        self.setFixedSize(300, 270)
        self.setWindowTitle("抽屉布局")
        container = QVBoxLayout()

        widget = QWidget()
        widget.setLayout(self.stacked_layout)
        widget.setStyleSheet("background-color:grey;")
        container.addWidget(widget)

        btn1 = QPushButton("抽屉1")
        btn2 = QPushButton("抽屉2")
        btn1.clicked.connect(self.btn1_clicked)
        btn2.clicked.connect(self.btn2_clicked)

        container.addWidget(btn1)
        container.addWidget(btn2)

        self.setLayout(container)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec()
