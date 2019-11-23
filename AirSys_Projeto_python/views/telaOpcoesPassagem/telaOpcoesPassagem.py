# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaOpcoesPassagem.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append("../../")
import views.recursos.recursos_rc


class Ui_telaOpcoesPassagem(object):
    def setupUi(self, telaOpcoesPassagem):
        telaOpcoesPassagem.setObjectName("telaOpcoesPassagem")
        telaOpcoesPassagem.resize(311, 321)
        telaOpcoesPassagem.setMinimumSize(QtCore.QSize(311, 321))
        telaOpcoesPassagem.setMaximumSize(QtCore.QSize(311, 321))
        telaOpcoesPassagem.setStyleSheet("#telaOpcoesPassagem\n"
                                         "{\n"
                                         "background-image: url(:/fundos/fundo3.jpg);\n"
                                         "}\n"
                                         "\n"
                                         "#botaoGerenciar\n"
                                         "{\n"
                                         "border-radius: 5px;\n"
                                         "background-color: rgb(12, 123, 157);\n"
                                         "font: 12pt \"Noto Serif Malayalam\";\n"
                                         "}\n"
                                         "\n"
                                         "#botaoGerenciar:hover\n"
                                         "{\n"
                                         "border-radius: 5px;\n"
                                         "background-color: rgb(145, 206, 243);\n"
                                         "font: 12pt \"Noto Serif Malayalam\";\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "#botaoConsultar\n"
                                         "{\n"
                                         "border-radius: 5px;\n"
                                         "background-color: rgb(12, 123, 157);\n"
                                         "font: 12pt \"Noto Serif Malayalam\";\n"
                                         "}\n"
                                         "\n"
                                         "#botaoConsultar:hover\n"
                                         "{\n"
                                         "border-radius: 5px;\n"
                                         "background-color: rgb(145, 206, 243);\n"
                                         "font: 12pt \"Noto Serif Malayalam\";\n"
                                         "}\n"
                                         "\n"
                                         "#botaoVoltar\n"
                                         "{\n"
                                         "border-radius: 5px;\n"
                                         "background-color: rgb(75, 117, 232);\n"
                                         "font: 12pt \"Noto Serif Malayalam\";\n"
                                         "}\n"
                                         "\n"
                                         "#botaoVoltar:hover\n"
                                         "{\n"
                                         "border-radius: 5px;\n"
                                         "background-color: rgb(121, 173, 255);\n"
                                         "font: 12pt \"Noto Serif Malayalam\";\n"
                                         "}\n"
                                         "")
        self.centralwidget = QtWidgets.QWidget(telaOpcoesPassagem)
        self.centralwidget.setObjectName("centralwidget")
        self.botaoGerenciar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoGerenciar.setGeometry(QtCore.QRect(40, 50, 221, 71))
        self.botaoGerenciar.setObjectName("botaoGerenciar")
        self.botaoConsultar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoConsultar.setGeometry(QtCore.QRect(40, 140, 221, 71))
        self.botaoConsultar.setObjectName("botaoConsultar")
        self.botaoVoltar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoVoltar.setGeometry(QtCore.QRect(80, 250, 151, 31))
        self.botaoVoltar.setObjectName("botaoVoltar")
        telaOpcoesPassagem.setCentralWidget(self.centralwidget)

        self.retranslateUi(telaOpcoesPassagem)
        QtCore.QMetaObject.connectSlotsByName(telaOpcoesPassagem)

    def retranslateUi(self, telaOpcoesPassagem):
        _translate = QtCore.QCoreApplication.translate
        telaOpcoesPassagem.setWindowTitle(
            _translate("telaOpcoesPassagem", "AirSys"))
        self.botaoGerenciar.setText(_translate(
            "telaOpcoesPassagem", "Gerenciar Passagens"))
        self.botaoConsultar.setText(_translate(
            "telaOpcoesPassagem", "Consultar Passagens"))
        self.botaoVoltar.setText(_translate("telaOpcoesPassagem", "Voltar"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    telaOpcoesPassagem = QtWidgets.QMainWindow()
    ui = Ui_telaOpcoesPassagem()
    ui.setupUi(telaOpcoesPassagem)
    telaOpcoesPassagem.show()
    sys.exit(app.exec_())
