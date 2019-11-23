# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaMenuGerente.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

sys.path.append("../../")
import views.recursos.recursos_rc


class Ui_telaOpcoesGerente(QtWidgets.QTabWidget):
    def setupUi(self, telaOpcoesGerente):
        telaOpcoesGerente.setObjectName("telaOpcoesGerente")
        telaOpcoesGerente.resize(381, 505)
        telaOpcoesGerente.setStyleSheet("#telaOpcoesGerente\n"
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
                                        "#botaoSair\n"
                                        "{\n"
                                        "border-radius: 5px;\n"
                                        "background-color: rgb(75, 117, 232);\n"
                                        "font: 14pt \"Noto Serif Malayalam\";\n"
                                        "}\n"
                                        "\n"
                                        "#botaoSair:hover\n"
                                        "{\n"
                                        "border-radius: 5px;\n"
                                        "background-color: rgb(121, 173, 255);\n"
                                        "font: 14pt \"Noto Serif Malayalam\";\n"
                                        "}")
        self.centralwidget = QtWidgets.QWidget(telaOpcoesGerente)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 30, 301, 461))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.botaoFuncionarios = QtWidgets.QPushButton(self.frame)
        self.botaoFuncionarios.setGeometry(QtCore.QRect(30, 40, 231, 81))
        self.botaoFuncionarios.setObjectName("botaoFuncionarios")
        self.botaoClientes = QtWidgets.QPushButton(self.frame)
        self.botaoClientes.setGeometry(QtCore.QRect(30, 150, 231, 81))
        self.botaoClientes.setObjectName("botaoClientes")
        self.botaoPassagens = QtWidgets.QPushButton(self.frame)
        self.botaoPassagens.setGeometry(QtCore.QRect(30, 260, 231, 81))
        self.botaoPassagens.setObjectName("botaoPassagens")
        self.botaoSair = QtWidgets.QPushButton(self.frame)
        self.botaoSair.setGeometry(QtCore.QRect(30, 410, 231, 25))
        self.botaoSair.setObjectName("botaoSair")
        telaOpcoesGerente.setCentralWidget(self.centralwidget)

        self.retranslateUi(telaOpcoesGerente)
        QtCore.QMetaObject.connectSlotsByName(telaOpcoesGerente)

    def retranslateUi(self, telaOpcoesGerente):
        _translate = QtCore.QCoreApplication.translate
        telaOpcoesGerente.setWindowTitle(
            _translate("telaOpcoesGerente", "AirSys"))
        self.botaoFuncionarios.setText(
            _translate("telaOpcoesGerente", "Funcionarios"))
        self.botaoClientes.setText(_translate("telaOpcoesGerente", "Clientes"))
        self.botaoPassagens.setText(
            _translate("telaOpcoesGerente", "Passagens"))
        self.botaoSair.setText(_translate("telaOpcoesGerente", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    telaOpcoesGerente = QtWidgets.QMainWindow()
    ui = Ui_telaOpcoesGerente()
    ui.setupUi(telaOpcoesGerente)
    telaOpcoesGerente.show()
    sys.exit(app.exec_())
