import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QGridLayout,
    QVBoxLayout,
)


class MyWindow(QWidget):
    my_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()

    def refresh_edit(self, msg):
        # :TODO
        print(msg)

    def a_button_clicked(self):
        # :TODO
        pass
    def init_ui(self):
        self.setWindowTitle("计算器")
        data = {
            0: ["7", "8", "9", "+", "("],
            1: ["4", "5", "6", "-", ")"],
            2: ["1", "2", "3", "*", "<-"],
            3: ["0", ".", "=", "/", "C"],
        }

        container = QVBoxLayout()
        edit = QLineEdit()
        edit.setPlaceholderText("请输入内容")
        container.addWidget(edit)

        grid = QGridLayout()

        for line_number, line_data in data.items():
            print(line_data)
            for col_number, number in enumerate(line_data):
                btn = QPushButton(number)
                grid.addWidget(btn, line_number, col_number)
        container.addLayout(grid)
        self.setLayout(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec()
