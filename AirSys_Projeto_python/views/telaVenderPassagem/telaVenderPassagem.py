# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaVenderPassagem.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append("../../")
import views.recursos.recursos_rc
import controles


class Ui_telaVendaPassagem(object):
    def __init__(self, objConsulta, codPassagem):
        self.objConsulta = objConsulta
        self.codPassagem = codPassagem

    def vender(self):
        pList = controles.ListaPassagens()
        passagem = pList.alterarPassagem(
            codigo=self.codPassagem,
            campo="estado",
            valor="comprada"
        )
        print("Passagem {0} vendida!".format(self.codPassagem))

    def setupUi(self, telaVendaPassagem):
        telaVendaPassagem.setObjectName("telaVendaPassagem")
        telaVendaPassagem.resize(353, 259)
        telaVendaPassagem.setMinimumSize(QtCore.QSize(353, 259))
        telaVendaPassagem.setMaximumSize(QtCore.QSize(353, 259))
        telaVendaPassagem.setStyleSheet("#telaVendaPassagem\n"
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
                                        "#botaoVender\n"
                                        "{\n"
                                        "font: 11pt \"Noto Serif Malayalam\";\n"
                                        "border-radius:3px;\n"
                                        "background-color: rgb(52, 95, 175);\n"
                                        "}\n"
                                        "\n"
                                        "#botaoVender:hover\n"
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
        self.centralwidget = QtWidgets.QWidget(telaVendaPassagem)
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
        self.botaoVender = QtWidgets.QPushButton(self.frame)
        self.botaoVender.setGeometry(QtCore.QRect(30, 140, 111, 31))
        self.botaoVender.setObjectName("botaoVender")
        self.botaoVender.clicked.connect(self.vender)
        self.botaoCancelar = QtWidgets.QPushButton(self.frame)
        self.botaoCancelar.setGeometry(QtCore.QRect(160, 140, 111, 31))
        self.botaoCancelar.setObjectName("botaoCancelar")
        self.botaoCancelar.clicked.connect(telaVendaPassagem.close)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(110, 90, 131, 17))
        self.label_3.setObjectName("label_3")
        telaVendaPassagem.setCentralWidget(self.centralwidget)

        self.retranslateUi(telaVendaPassagem)
        QtCore.QMetaObject.connectSlotsByName(telaVendaPassagem)

    def retranslateUi(self, telaVendaPassagem):
        _translate = QtCore.QCoreApplication.translate
        telaVendaPassagem.setWindowTitle(_translate(
            "telaVendaPassagem", "Vender Passsagem"))
        self.label.setText(_translate("telaVendaPassagem",
                                      "Confirmar venda da passagem:"))
        self.label_2.setText(_translate("telaVendaPassagem", "Codigo:"))
        self.botaoVender.setText(_translate("telaVendaPassagem", "Vender"))
        self.botaoCancelar.setText(_translate("telaVendaPassagem", "Cancelar"))
        self.label_3.setText(_translate("telaVendaPassagem", self.codPassagem))
"""

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    telaVendaPassagem = QtWidgets.QMainWindow()
    ui = Ui_telaVendaPassagem()
    ui.setupUi(telaVendaPassagem)
    telaVendaPassagem.show()
    sys.exit(app.exec_())
"""