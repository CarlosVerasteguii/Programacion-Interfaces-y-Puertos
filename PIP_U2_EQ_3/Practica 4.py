import sys
import random
from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = "Practica4.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btnIniciar.clicked.connect(self.iniciar)
        self.btnIniciar.clicked.connect(self.realizarSuma)
        self.btn_Revisar.clicked.connect(self.revisar)

        # Contador de aciertos
        self.contador = 0

    # Área de los slots
    def iniciar(self):
        try:
            rnd_num1 = random.randint(1, 100)
            rnd_num2 = random.randint(1, 100)
            self.Rnd1.setText(str(rnd_num1))
            # Selección aleatoria entre + y -
            symbol = random.choice(["+", "-"])
            self.Rnd2.setText(symbol)
            self.Rnd3.setText(str(rnd_num2))
        except Exception as error:
            print(error)

    def realizarSuma(self):
        try:
            a = int(self.Rnd1.text())
            b = int(self.Rnd3.text())
            if self.Rnd2.text() == "+":
                resultado = a + b
            else:
                resultado = a - b
            self.txt_R.setPlainText(str(resultado))
        except Exception as error:
            print(error)

    def revisar(self):
        try:
            r_Usua = int(self.r_Usu.toPlainText())
            r_Si = int(self.txt_R.toPlainText())
            if r_Usua == r_Si:
                self.aciertos.setText("Correcto")
                self.contador += 1
                self.lbl_contador.setText(str(self.contador))
            else:
                self.aciertos.setText("Incorrecto")
        except Exception as error:
            print(error)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
