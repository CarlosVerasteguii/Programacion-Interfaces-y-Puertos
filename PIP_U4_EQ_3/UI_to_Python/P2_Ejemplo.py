# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P2_Ejemplo.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("\n"
"\n"
"background-color: rgb(139, 184, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_saludar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_saludar.setGeometry(QtCore.QRect(110, 400, 301, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_saludar.setFont(font)
        self.btn_saludar.setStyleSheet("background-color: rgb(193, 255, 126);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);\n"
"border-radius:20px;\n"
"border: 4px solid white;\n"
"")
        self.btn_saludar.setObjectName("btn_saludar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 190, 171, 81))
        self.label.setObjectName("label")
        self.txt_nombre = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_nombre.setGeometry(QtCore.QRect(270, 210, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.txt_nombre.setFont(font)
        self.txt_nombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_nombre.setText("")
        self.txt_nombre.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_nombre.setObjectName("txt_nombre")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_saludar.setText(_translate("MainWindow", "Saludar"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600; color:#006a00;\">Nombre:</span></p></body></html>"))
