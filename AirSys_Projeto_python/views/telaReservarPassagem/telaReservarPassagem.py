# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaReservarPassagem.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append("../../")
import views.recursos.recursos_rc
import controles


class Ui_telaReservaPassagem(object):
    def __init__(self, objConsulta, codPassagem):
        self.objConsulta = objConsulta
        self.codPassagem = codPassagem

    def reservar(self):
        pList = controles.ListaPassagens()
        passagem = pList.alterarPassagem(
            codigo=self.codPassagem,
            campo="estado",
            valor="reservada"
        )
        # print("Passagem {0} reservada!".format(self.codPassagem))
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Aviso")
        msgBox.setText("Passagem {0} reservada!".format(self.codPassagem))
        msgBox.exec_()

    def setupUi(self, telaReservaPassagem):
        telaReservaPassagem.setObjectName("telaReservaPassagem")
        telaReservaPassagem.resize(353, 259)
        telaReservaPassagem.setMinimumSize(QtCore.QSize(353, 259))
        telaReservaPassagem.setMaximumSize(QtCore.QSize(353, 259))
        telaReservaPassagem.setStyleSheet("#telaReservaPassagem\n"
                                          "{\n"
                                          "background-image: url(:/fundos/fundo3.jpg);\n"
                                          "}\n"
                                          "#frame\n"
                                          "{\n"
                                          "border-radius:3px;\n"
                                          "background-color: rgba(165, 180, 222, 180);\n"
                                          "}\n"
                                          "#label\n"
                                          "{\n"
                                          "font: 11pt \"Noto Serif Malayalam\";\n"
                                          "color: rgb(3, 33, 43);\n"
                                          "}\n"
                                          "#label_2\n"
                                          "{\n"
                                          "font: 11pt \"Noto Serif Malayalam\";\n"
                                          "color: rgb(3, 33, 43);\n"
                                          "}\n"
                                          "\n"
                                          "#label_3\n"
                                          "{\n"
                                          "font: 11pt \"Noto Serif Malayalam\";\n"
                                          "    color: rgb(187, 68, 48);\n"
                                          "}\n"
                                          "\n"
                                          "#botaoReservar\n"
                                          "{\n"
                                          "font: 11pt \"Noto Serif Malayalam\";\n"
                                          "border-radius:3px;\n"
                                          "background-color: rgb(52, 95, 175);\n"
                                          "}\n"
                                          "\n"
                                          "#botaoReservar:hover\n"
                                          "{\n"
                                          "background-color: rgb(120, 162, 239);\n"
                                          "}\n"
                                          "\n"
                                          "#botaoCancelar\n"
                                          "{\n"
                                          "font: 11pt \"Noto Serif Malayalam\";\n"
                                          "border-radius:3px;\n"
                                          "background-color: rgb(52, 95, 175);\n"
                                          "}\n"
                                          "\n"
                                          "#botaoCancelar:hover\n"
                                          "{\n"
                                          "background-color: rgb(120, 162, 239);\n"
                                          "}\n"
                                          "")
        self.centralwidget = QtWidgets.QWidget(telaReservaPassagem)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 291, 201))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 20, 231, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 54, 17))
        self.label_2.setObjectName("label_2")
        self.botaoReservar = QtWidgets.QPushButton(self.frame)
        self.botaoReservar.setGeometry(QtCore.QRect(30, 140, 111, 31))
        self.botaoReservar.setObjectName("botaoReservar")
        self.botaoReservar.clicked.connect(self.reservar)
        self.botaoCancelar = QtWidgets.QPushButton(self.frame)
        self.botaoCancelar.setGeometry(QtCore.QRect(160, 140, 111, 31))
        self.botaoCancelar.setObjectName("botaoCancelar")
        self.botaoCancelar.clicked.connect(telaReservaPassagem.close)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(110, 90, 141, 16))
        self.label_3.setObjectName("label_3")
        telaReservaPassagem.setCentralWidget(self.centralwidget)

        self.retranslateUi(telaReservaPassagem)
        QtCore.QMetaObject.connectSlotsByName(telaReservaPassagem)

    def retranslateUi(self, telaReservaPassagem):
        _translate = QtCore.QCoreApplication.translate
        telaReservaPassagem.setWindowTitle(_translate(
            "telaReservaPassagem", "Reservar Passagem"))
        self.label.setText(_translate("telaReservaPassagem",
                                      "Confirmar reserva da passagem:"))
        self.label_2.setText(_translate("telaReservaPassagem", "Codigo:"))
        self.botaoReservar.setText(_translate(
            "telaReservaPassagem", "Reservar"))
        self.botaoCancelar.setText(_translate(
            "telaReservaPassagem", "Cancelar"))
        self.label_3.setText(_translate("telaReservaPassagem", self.codPassagem))

"""
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    telaReservaPassagem = QtWidgets.QMainWindow()
    ui = Ui_telaReservaPassagem()
    ui.setupUi(telaReservaPassagem)
    telaReservaPassagem.show()
    sys.exit(app.exec_())
"""