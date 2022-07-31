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



"""
Si dos carpetas, una tuya y una mia
recien me acuerdo que se puede comentar así XD
Jajajaajj entiendo XDD
deja hago las carpetas
"""
"""
Estaba pensando mas adelante hacer una plantilla para las practicas
así no copiamos el codigo basico a cada rato. pero será después
"""

# if __name__ == "__main__":
#     main()

