import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Prog_03_Promedio.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcular)

    # Área de los Slots
    def calcular(self):
        try:
            n1 = float(self.txt_prom1.text())
            n2 = float(self.txt_prom2.text())
            n3 = float(self.txt_prom3.text())
            n4 = float(self.txt_prom4.text())
            n5 = float(self.txt_prom5.text())

            promedio = (n1 + n2 + n3 + n4 + n5) / 5
            self.txt_res.setText("{:.2f}".format(promedio))
        except Exception as error:
            print(error)
            return None


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())