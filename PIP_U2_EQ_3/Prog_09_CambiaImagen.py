import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Prog_09_CambiaImagen.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.slider_img.setMinimum(0)
        self.slider_img.setMaximum(4)
        self.slider_img.setSingleStep(0)
        self.slider_img.setValue(0)

        self.slider_img.valueChanged.connect(self.cambiaImagen)

        self.listaImgs = []
        self.listaImgs.append(["coca", "ruta"])
        self.listaImgs.append(["chips", "ruta"])
        self.listaImgs.append(["jugo", "ruta"])
        self.listaImgs.append(["epura", "ruta"])
        self.listaImgs.append(["panditas", "ruta"])

        self.txt_valorA.setText("")



    # Área de los slots
    def cambiaImagen(self):
        imagen = self.listaImgs[self.slider_img.value()]
        self.txt_valorA.setText(imagen[0])
        #self.txt_valorA.setText(str(self.slider_img.value()))







if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())