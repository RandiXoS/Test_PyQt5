import os
import sys
from PyQt5 import QtWidgets, QtCore, QtGui



def Init():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("Hello World")
    window.resize(300, 300)
    window.show()
    sys.exit(app.exec_())



def main():
    Init()

main()
