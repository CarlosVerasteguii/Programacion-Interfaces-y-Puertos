import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "Prog_10_CalcUnid.ui" # Nombre del archivo aquí
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

def distanciaa(x1, y1, x2, y2):
    distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return distancia

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
            numero = int(self.txt_num.text())
            unidades = numero % 10
            decenas = (numero // 10) % 10
            centenas = numero // 100

            self.txt_resu.setText(str(unidades)+" Unidades")
            self.txt_resd.setText(str(decenas)+" Decenas")
            self.txt_resc.setText(str(centenas)+" Centenas")
        except Exception as error:
                print(error)
                return None


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
