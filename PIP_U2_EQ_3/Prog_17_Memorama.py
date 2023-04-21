from QLabelClickeable import clickable

import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "Prog_17_Memorama.ui" #nombre del archivo aqui.
Ui_MainWindow, QtBaseCLass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        clickable(self.img1).connect(self.clicImage1)
        clickable(self.img2).connect(self.clicImage2)
        clickable(self.img3).connect(self.clicImage3)
        clickable(self.img4).connect(self.clicImage4)

        self.listaIamgenesDisponibles = [
            [0, ":/Comidas/chips.png"],
            [1, ":/Comidas/takis.png"],
        ]

        self.contMax= 2
        self.ordenImagenesMemorama = [];
        self.estadoTarjetas = [] #determina si la tarjeta se puede voltear o no
        for i in self.listaIamgenesDisponibles:
            for j in range(self.contMax):
                self.ordenImagenesMemorama.append(i[0])
                self.estadoTarjetas.append(True)

        #print(ordenImagenesMemorama)

        import random as rnd
        rnd.shuffle(self.ordenImagenesMemorama)
        print(self.ordenImagenesMemorama)

        self.btn_validar.clicked.connect(self.validar)

        self.tarjetaVolteada = 0

    def mensajeEmergente(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

    def clicImage1(self):
        try:
            if self.tarjetaVolteada < self.contMax:
                self.img1.setPixmap(QtGui.QPixmap( #corregir img2
                    self.listaIamgenesDisponibles[self.ordenImagenesMemorama[0]][1]
                ))
                self.tarjetaVolteada += 1
                self.estadoTarjetas[0] = False

        except Exception as error:
            print(error)
            return None

    def clicImage2(self):
        #self.mensajeEmergente("imagen 2")
        try:
            if self.tarjetaVolteada < self.contMax:
                self.img2.setPixmap(QtGui.QPixmap(
                    self.listaIamgenesDisponibles[self.ordenImagenesMemorama[1]][1]
                ))
                self.tarjetaVolteada += 1
                self.estadoTarjetas[0] = False

        except Exception as error:
            print(error)
            return None

    def clicImage3(self):
        try:
            if self.tarjetaVolteada < self.contMax:
                self.img3.setPixmap(QtGui.QPixmap(
                    self.listaIamgenesDisponibles[self.ordenImagenesMemorama[2]][1]
                ))
                self.tarjetaVolteada += 1
                self.estadoTarjetas[0] = False

        except Exception as error:
            print(error)
            return None

    def clicImage4(self):
        try:
            if self.tarjetaVolteada < self.contMax:
                self.img4.setPixmap(QtGui.QPixmap(
                    self.listaIamgenesDisponibles[self.ordenImagenesMemorama[3]][1]
                ))
                self.tarjetaVolteada += 1
                self.estadoTarjetas[0] = False

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