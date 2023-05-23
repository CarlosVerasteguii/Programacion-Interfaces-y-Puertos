import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "P11_Prom.ui"  # Ruta relativa del archivo P11_Prom.ui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_agregar.clicked.connect(self.agregar_edad)
        self.edades = []

        # Establecer valor predeterminado para la cantidad de alumnos
        self.le_n.setText("5")

    def agregar_edad(self):
        # Obtener el número de alumnos
        n_alumnos = self.le_n.text()
        if not n_alumnos:
            n_alumnos = 5  # Valor predeterminado si el campo está vacío
        try:
            n_alumnos = int(n_alumnos)
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Error", "Ingrese un número válido de alumnos.")
            return

        # Bloquear las señales de le_edades
        self.le_edades.blockSignals(True)

        # Obtener las edades ingresadas
        edades_texto = self.le_edades.text()
        edades_ingresadas = edades_texto.split(",")
        if len(edades_ingresadas) != n_alumnos:
            QtWidgets.QMessageBox.warning(self, "Error", f"Ingrese {n_alumnos} edades.")
            self.le_edades.blockSignals(False)  # Desbloquear las señales de le_edades
            return

        # Convertir las edades a enteros
        try:
            edades = [int(edad) for edad in edades_ingresadas]
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Error", "Ingrese edades válidas.")
            self.le_edades.blockSignals(False)  # Desbloquear las señales de le_edades
            return

        # Calcular el promedio de las edades
        promedio = sum(edades) / n_alumnos

        # Mostrar el promedio
        self.l_promedio.setText(f"Promedio: {promedio:.2f}")

        # Desbloquear las señales de le_edades
        self.le_edades.blockSignals(False)

        # Agregar las edades al arreglo para mantener un seguimiento
        self.edades.extend(edades)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
