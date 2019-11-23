# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaOpcoesFuncionario.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append("../../")
import views.recursos.recursos_rc

class Ui_telaOpcoesFuncionario(object):
    def setupUi(self, telaOpcoesFuncionario):
        telaOpcoesFuncionario.setObjectName("telaOpcoesFuncionario")
        telaOpcoesFuncionario.resize(381, 505)
        telaOpcoesFuncionario.setStyleSheet("#telaOpcoesFuncionario\n"
                                            "{\n"
                                            "background-image: url(:/fundos/fundo4.jpg);\n"
                                            "}\n"
                                            "\n"
                                            "#frame\n"
                                            "{\n"
                                            "background-color: rgba(6, 190, 225, 70);\n"
                                            "}\n"
                                            "\n"
                                            "#botaoFuncionarios\n"
                                            "{\n"
                                            "border-radius: 5px;\n"
                                            "background-color: rgb(12, 123, 157);\n"
                                            "font: 14pt \"Noto Serif Malayalam\";\n"
                                            "}\n"
                                            "\n"
                                            "#botaoFuncionarios:hover\n"
                                            "{\n"
                                            "border-radius: 5px;\n"
                                            "background-color: rgb(145, 206, 243);\n"
                                            "font: 14pt \"Noto Serif Malayalam\";\n"
                                            "}\n"
                                            "\n"
                                            "#botaoClientes\n"
                                            "{\n"
                                            "border-radius: 5px;\n"
                                            "background-color: rgb(12, 123, 157);\n"
                                            "font: 14pt \"Noto Serif Malayalam\";\n"
                                            "}\n"
                                            "\n"
                                            "#botaoClientes:hover\n"
                                            "{\n"
                                            "border-radius: 5px;\n"
                                            "background-color: rgb(145, 206, 243);\n"
                                            "font: 14pt \"Noto Serif Malayalam\";\n"
                                            "}\n"
                                            "\n"
                                            "#botaoPassagens\n"
                                            "{\n"
                                            "border-radius: 5px;\n"
                                            "background-color: rgb(12, 123, 157);\n"
                                            "font: 14pt \"Noto Serif Malayalam\";\n"
                                            "}\n"
                                            "\n"
                                            "#botaoPassagens:hover\n"
                                            "{\n"
                                            "border-radius: 5px;\n"
                                            "background-color: rgb(145, 206, 243);\n"
                                            "font: 14pt \"Noto Serif Malayalam\";\n"
                                            "}\n"
                                            "\n"
                                            "#botaoVoltar\n"
                                            "{\n"
                                            "border-radius: 5px;\n"
                                            "background-color: rgb(75, 117, 232);\n"
                                            "font: 14pt \"Noto Serif Malayalam\";\n"
                                            "}\n"
                                            "\n"
                                            "#botaoVoltar:hover\n"
                                            "{\n"
                                            "border-radius: 5px;\n"
                                            "background-color: rgb(121, 173, 255);\n"
                                            "font: 14pt \"Noto Serif Malayalam\";\n"
                                            "}")
        self.centralwidget = QtWidgets.QWidget(telaOpcoesFuncionario)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 30, 301, 461))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.botaoClientes = QtWidgets.QPushButton(self.frame)
        self.botaoClientes.setGeometry(QtCore.QRect(30, 60, 231, 101))
        self.botaoClientes.setObjectName("botaoClientes")
        self.botaoPassagens = QtWidgets.QPushButton(self.frame)
        self.botaoPassagens.setGeometry(QtCore.QRect(30, 230, 231, 101))
        self.botaoPassagens.setObjectName("botaoPassagens")
        self.botaoVoltar = QtWidgets.QPushButton(self.frame)
        self.botaoVoltar.setGeometry(QtCore.QRect(30, 410, 231, 25))
        self.botaoVoltar.setObjectName("botaoVoltar")
        telaOpcoesFuncionario.setCentralWidget(self.centralwidget)

        self.retranslateUi(telaOpcoesFuncionario)
        QtCore.QMetaObject.connectSlotsByName(telaOpcoesFuncionario)

    def retranslateUi(self, telaOpcoesFuncionario):
        _translate = QtCore.QCoreApplication.translate
        telaOpcoesFuncionario.setWindowTitle(
            _translate("telaOpcoesFuncionario", "AirSys"))
        self.botaoClientes.setText(_translate(
            "telaOpcoesFuncionario", "Clientes"))
        self.botaoPassagens.setText(_translate(
            "telaOpcoesFuncionario", "Passagens"))
        self.botaoVoltar.setText(_translate("telaOpcoesFuncionario", "Voltar"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    telaOpcoesFuncionario = QtWidgets.QMainWindow()
    ui = Ui_telaOpcoesFuncionario()
    ui.setupUi(telaOpcoesFuncionario)
    telaOpcoesFuncionario.show()
    sys.exit(app.exec_())
