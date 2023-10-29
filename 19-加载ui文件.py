import sys

from PyQt5.QtWidgets import  QApplication
from  PyQt5 import uic


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = uic.loadUi("./test.ui")
    w.show()
    app.exec()