import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "Prog_04_PuntoMedio.ui" # Nombre del archivo aquí
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
            x1 = float(self.txt_x1.text())
            y1 = float(self.txt_y1.text())
            x2 = float(self.txt_x2.text())
            y2 = float(self.txt_y2.text())

            xm = (x1 + x2) / 2
            ym = (y1 + y2) / 2
            self.txt_resx.setText("{:.2f}".format(xm))
            self.txt_resy.setText("{:.2f}".format(ym))
        except Exception as error:
            print(error)
            return None


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
