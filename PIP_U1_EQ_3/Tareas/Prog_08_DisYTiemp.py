import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "Prog_08_DisYTiemp.ui" # Nombre del archivo aquí
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
            t = float(self.txt_t.text())
            d = float(self.txt_d.text())
            v = d / t
            self.txt_res.setText("{:.2f}".format(v))
        except Exception as error:
            print(error)
            return None

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
