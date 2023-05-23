import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "P1_Hamburguesas.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.cb_tipo_burguesa.addItem("H. Sencilla",1)
        self.cb_tipo_burguesa.addItem("H. Doble", 2)
        self.cb_tipo_burguesa.addItem("H. Triple", 3)

                                       # [ 0,  1]
        self.cantHamburguesasXtipo = { #ID : [contador, costo]
                                      1: [0, 20],
                                      2: [0, 25],
                                      3: [0, 30]}
        self.btn_agregar.clicked.connect(self.agregar)

        self.importe = 0

    # Área de los slots
    def agregar(self):
        try:
            cantidad = int(self.txt_cantidad.text())
            tipo=self.cb_tipo_burguesa.currentData()
            print("Tipo: ", tipo, "  Cantidad: ",cantidad)


            self.datosTipoXHamburguesa = self.cantHamburguesasXtipo[tipo]
            #                         cantidad * costo del tripo de hamburguesa sleecionada
            totalXHamburguesas = cantidad * self.datosTipoXHamburguesa[1]

            self.datosTipoXHamburguesa[0] += cantidad #actualiza de ham por tipo

            self.importe += totalXHamburguesas #acumula el importe

            tempCantidad = str(self.datosTipoXHamburguesa[0]) #convierte en string la cantidad para mandar a la caja de texto
            if tipo==1:
                self.txt_cantidad_sencillas.setText(tempCantidad)
            elif tipo==2:
                self.txt_cantidad_dobles.setText(tempCantidad)
            else:
                self.txt_cantidad_triples.setText(tempCantidad)

            self.txt_importe.setText(str(self.importe))
        except ValueError:
            print("Error: La cantidad debe ser un número entero.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
