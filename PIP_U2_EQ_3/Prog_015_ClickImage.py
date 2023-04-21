from QLabelClickeable import clickable

import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
qtCreatorFile = "Prog_015_ClickImage.ui" #nombre del archivo aqui.
Ui_MainWindow, QtBaseCLass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #self.img.clicked.connect(self.clickImage) #No se puede con labels
        clickable(self.img).connect(self.clicImage)

        self.btn_borrar.clicked.connect(self.borrar)

    def clicImage(self):
        print("Hiciste click")
        self.txt_Nombre.setText("Paco")
        self.txt_Edad.setText("6")
        self.txt_Ocupacion.setText("Asesino")

    def borrar(self):
        self.txt_Nombre.setText("")
        self.txt_Edad.setText("")
        self.txt_Ocupacion.setText("")

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())