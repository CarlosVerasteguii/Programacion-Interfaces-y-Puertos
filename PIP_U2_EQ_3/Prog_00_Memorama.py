from PyQt5 import QtWidgets, QtGui, QtCore
from QLabelClickeable import clickable
import random as rnd

qtCreatorFile = "Prog_17_Memorama.ui" #nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Conectamos los clicks en las imágenes con los correspondientes métodos
        clickable(self.img1).connect(self.clicImage1)
        clickable(self.img2).connect(self.clicImage2)
        clickable(self.img3).connect(self.clicImage3)
        clickable(self.img4).connect(self.clicImage4)

        # Creamos una lista con las imágenes disponibles y su id
        self.listaIamgenesDisponibles = [
            [0, ":/Comidas/chips.png"],
            [1, ":/Comidas/takis.png"]
        ]

        self.contMax = 2  # Número de pares de tarjetas
        self.ordenImagenesMemorama = []  # Lista que contiene el orden de las imágenes
        self.estadoTarjetas = []  # Lista que determina si la tarjeta se puede voltear o no

        # Agregamos los pares de tarjetas a la lista de orden de imágenes y su estado correspondiente
        for i in self.listaIamgenesDisponibles:
            for j in range(self.contMax):
                self.ordenImagenesMemorama.append(i[0])
                self.estadoTarjetas.append(True)

        # Desordenamos la lista de orden de imágenes
        rnd.shuffle(self.ordenImagenesMemorama)

        self.btn_validar.clicked.connect(self.validar)
        self.tarjetaVolteada = 0

    def mensajeEmergente(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

    def clicImage1(self):
        try:
            if self.tarjetaVolteada < self.contMax and self.estadoTarjetas[0]:
                self.img1.setPixmap(QtGui.QPixmap(self.listaIamgenesDisponibles[self.ordenImagenesMemorama[0]][1]))
                self.tarjetaVolteada += 1
                self.estadoTarjetas[0] = False

        except Exception as error:
            print(error)
            return None

    def clicImage2(self):
        try:
            if self.tarjetaVolteada < self.contMax and self.estadoTarjetas[1]:
                self.img2.setPixmap(QtGui.QPixmap(self.listaIamgenesDisponibles[self.ordenImagenesMemorama[1]][1]))
                self.tarjetaVolteada += 1
                self.estadoTarjetas[1] = False

        except Exception as error:
            print(error)
            return None

    def clicImage3(self):
        try:
            if self.tarjetaVolteada < self.contMax and self.estadoTarjetas[2]:
                self.img3.setPixmap(QtGui.QPixmap(self.listaIamgenesDisponibles[self.ordenImagenesMemorama[2]][1]))
                self.tarjetaVolteada += 1
                self.estadoTarjetas[2] = False

        except Exception as error:
            print(error)
            return None

    def clicImage4(self):
        try:
            if self.tarjetaVolteada < self.contMax and self.estadoTarjetas[3]:
                self.img3.setPixmap(QtGui.QPixmap(self.listaIamgenesDisponibles[self.ordenImagenesMemorama[2]][1]))
                self.tarjetaVolteada += 1
                self.estadoTarjetas[3] = False

        except Exception as error:
            print(error)
            return None


    def validar(self):
        pass



if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())