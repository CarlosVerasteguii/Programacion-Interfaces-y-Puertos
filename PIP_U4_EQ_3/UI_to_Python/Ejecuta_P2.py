import sys
from PyQt5 import uic, QtWidgets, QtCore

from UI_to_Python import P2_Ejemplo as interfaz


class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_saludar.clicked.connect(self.saludar)

    # Área de los slots
    def saludar(self):
        self.mensaje("Hola!, Saludos :)")

    def mensaje(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())