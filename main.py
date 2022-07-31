import os
import sys
from PyQt5 import QtWidgets, QtCore, QtGui



#Config App
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


# y como practicamos??

if __name__ == "__main__":
    main()

