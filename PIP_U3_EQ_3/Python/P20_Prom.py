import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "P20_Prom.ui"  # Nombre del archivo aquí
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.edades_salon_a = []
        self.edades_salon_b = []

        self.btn_agregar.clicked.connect(self.agregar_edad)

    def agregar_edad(self):
        edad = self.le_Year.text()

        try:
            edad_entero = int(edad)

            if self.rb_A.isChecked():
                self.edades_salon_a.append(edad_entero)
                promedio_a = sum(self.edades_salon_a) / len(self.edades_salon_a)
                self.l_promA.setText(f"Salón A: {promedio_a:.2f}")
            elif self.rb_B.isChecked():
                self.edades_salon_b.append(edad_entero)
                promedio_b = sum(self.edades_salon_b) / len(self.edades_salon_b)
                self.l_promB.setText(f"Salón B: {promedio_b:.2f}")

            promedio_total = (sum(self.edades_salon_a) + sum(self.edades_salon_b)) / (
                        len(self.edades_salon_a) + len(self.edades_salon_b))
            self.l_promT.setText(f"Total: {promedio_total:.2f}")

            self.le_Year.clear()

        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Error", "Ingresa una edad válida.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())