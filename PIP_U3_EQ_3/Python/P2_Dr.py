import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "P2_Dr.ui"  # Nombre del archivo aquí
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_registrar.clicked.connect(self.registrar_cita)

    def registrar_cita(self):
        # Obtener el número de cita actual
        cita_actual = int(self.txt_ca.text())

        # Realizar los cálculos para determinar el costo de la cita y el total pagado
        if cita_actual <= 3:
            costo_cita_actual = 200.00
        elif cita_actual <= 5:
            costo_cita_actual = 150.00
        elif cita_actual <= 8:
            costo_cita_actual = 100.00
        else:
            costo_cita_actual = 50.00

        total_pagado = self.calcular_total_pagado(cita_actual)

        # Actualizar los valores en los QLineEdit correspondientes
        self.txt_cca.setText(str(costo_cita_actual))
        self.txt_tp.setText(str(total_pagado))

    def calcular_total_pagado(self, cita_actual):
        if cita_actual <= 3:
            return 200.00 * cita_actual
        elif cita_actual <= 5:
            return (200.00 * 3) + (150.00 * (cita_actual - 3))
        elif cita_actual <= 8:
            return (200.00 * 3) + (150.00 * 2) + (100.00 * (cita_actual - 5))
        else:
            return (200.00 * 3) + (150.00 * 2) + (100.00 * 3) + (50.00 * (cita_actual - 8))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
