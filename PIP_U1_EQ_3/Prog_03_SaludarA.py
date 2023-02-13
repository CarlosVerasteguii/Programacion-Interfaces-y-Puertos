import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Prog_03_SaludarA.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_saludar.clicked.connect(self.saludar)

    # Área de los slots
    def saludar(self):
        n = self.txt_nombre.text()
        self.mensaje("Hola! "+ n +", Saludos :)")

    def mensaje(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())