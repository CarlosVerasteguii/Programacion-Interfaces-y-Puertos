import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "P16_Año.ui"  # Nombre del archivo aquí
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_estimar.clicked.connect(self.estimar)

    def estimar(self):
        try:
            # Obtener el salario inicial
            salario_inicial = int(self.le_salario.text())

            tasa_incremento = 0.10
            años = 6

            salario_actual = salario_inicial
            salarios_x_año = []

            # Calcular incremento anual acumulado y actualizar los line edits
            for i in range(1, años + 1):
                incremento = salario_actual * tasa_incremento
                salario_actual += incremento
                salarios_x_año.append(salario_actual)
                line_edit = getattr(self, f"le_a{i}")
                line_edit.setText("{:.2f}".format(salario_actual))
        except ValueError:
            self.le_a1.setText("Caracter no válido")
            self.le_a2.setText("Caracter no válido")
            self.le_a3.setText("Caracter no válido")
            self.le_a4.setText("Caracter no válido")
            self.le_a5.setText("Caracter no válido")
            self.le_a6.setText("Caracter no válido")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
