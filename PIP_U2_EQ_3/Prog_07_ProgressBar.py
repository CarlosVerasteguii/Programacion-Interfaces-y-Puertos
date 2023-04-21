import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Prog_07_ProgressBar.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.progressBar.setMinimum  (0)
        self.progressBar.setMaximum  (100)
        self.progressBar.setValue(0)

        self.progressBar.valueChanged.connect(self.cambiaValor)
        self.txt_valor.setText("0")

        import time as t #para lo de que tarde en ejecutarse

        for i in range(100):
            self.progressBar.setValue(i)
            t.sleep(0.1) #para que el if tarde 20 milisegundos en ejecutarse

    # Área de los slots
    def cambiaValor(self):
        self.txt_valor.setText(str(self.progressBar.value()))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())