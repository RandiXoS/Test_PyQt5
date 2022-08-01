import os
import sys
from PyQt5 import QtWidgets, QtCore, QtGui



#Por cierto no se vale hacer copy paste de internet
def Init():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("Hello World")
    window.resize(300, 300)
    window.show()
    sys.exit(app.exec_())



def main():
    Init()
    #print("Hello World!")


