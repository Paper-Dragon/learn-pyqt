import sys
import time

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QScrollArea, QHBoxLayout, QPushButton


class MyWindow(QWidget):
    my_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.msg_history = list()

    def check(self):
        for i, ip in enumerate(["192.168.0.%d" % x for x in range(1, 20)]):
            msg = f"模拟， 正在检查{ip} ..."
            if i % 5 == 3:
                self.my_signal.emit(f"{msg} 发现问题！")
            time.sleep(0.05)

    def my_slot(self, msg):
        print(msg)
        self.msg_history.append(msg)
        self.msg.setText("<br>".join(self.msg_history))
        self.msg.resize(440, self.msg.frameSize().height()+15)
        self.msg.repaint()

    def init_ui(self):
        self.resize(500, 200)

        container = QVBoxLayout()

        self.msg = QLabel("")

        self.msg.resize(440, 15)
        print(self.msg.frameSize())
        self.msg.setWordWrap(True)
        self.msg.setAlignment(Qt.AlignTop)
        self.msg.setStyleSheet("background-color:yellow; color:black;")

        scroll = QScrollArea()
        scroll.setWidget(self.msg)

        v_layout = QVBoxLayout()
        v_layout.addWidget(scroll)

        h_layout = QHBoxLayout()
        btn = QPushButton("开始检测")
        btn.clicked.connect(self.check)

        h_layout.addStretch(1)
        h_layout.addWidget(btn)
        h_layout.addStretch(1)

        container.addLayout(v_layout)
        container.addLayout(h_layout)
        self.setLayout(container)

        self.my_signal.connect(self.my_slot)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec()
