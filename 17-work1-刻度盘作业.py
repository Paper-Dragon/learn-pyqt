from PyQt5.QtWidgets import QApplication, QWidget, QDial, QSpinBox, QHBoxLayout
import sys
from PyQt5.QtCore import pyqtSignal


class MyWindow(QWidget):
    dial1_signal = pyqtSignal(int)
    spinbox1_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.init_ui()

    def change_spinbox(self, value):
        self.my_spinbox.setValue(value)

    def change_dial(self, value):
        self.my_dial.setValue(value)

    def dial_value_changed(self, value):
        print(value)
        self.dial1_signal.emit(value)

    def spinbox_changed(self, value):
        print(value)
        self.spinbox1_signal.emit(value)

    def init_ui(self):
        self.setWindowTitle("刻度盘")
        self.setFixedSize(400, 100)
        container = QHBoxLayout()
        self.my_dial = QDial()
        self.my_dial.setRange(0, 100)
        self.my_dial.setNotchesVisible(True)
        self.my_dial.valueChanged.connect(self.dial_value_changed)

        self.my_spinbox = QSpinBox()
        self.my_spinbox.valueChanged.connect(self.spinbox_changed)

        container.addWidget(self.my_dial)
        container.addWidget(self.my_spinbox)
        self.setLayout(container)
        self.dial1_signal.connect(self.change_spinbox)
        self.spinbox1_signal.connect(self.change_dial)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec()
