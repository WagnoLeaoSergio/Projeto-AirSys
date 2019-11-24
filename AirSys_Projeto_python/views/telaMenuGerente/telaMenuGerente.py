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
    def switchToFuncionario(self, ui):
        from views.telaGerenciarFuncionario.telaGerenciarFuncionario import Ui_telaGerenciarFuncionario
        self.telaMenu = QtWidgets.QMainWindow()
        self.menuFuncionario = Ui_telaGerenciarFuncionario()
        self.menuFuncionario.setupUi(self.telaMenu)
        ui.hide()
        self.telaMenu.show()

    def switchToClientes(self, ui):
        from views.telaGerenciarCliente.telaGerenciarCliente import Ui_telaGerenciarCliente
        self.telaMenu = QtWidgets.QMainWindow()
        self.menuCliente = Ui_telaGerenciarCliente()
        self.menuCliente.setupUi(self.telaMenu)
        self.menuCliente.setTelaAnterior("Gerente")
        ui.hide()
        self.telaMenu.show()

    def switchToPassagem(self, ui):
        from views.telaOpcoesPassagem.telaOpcoesPassagem import Ui_telaOpcoesPassagem
        self.telaMenu = QtWidgets.QMainWindow()
        self.menuPassagem = Ui_telaOpcoesPassagem()
        self.menuPassagem.setupUi(self.telaMenu)
        self.menuPassagem.setTelaAnterior("Gerente")
        ui.hide()
        self.telaMenu.show()

    def switchVoltar(self, ui):
        from views.telaLogin.telaLogin import Ui_Login
        tela = QtWidgets.QMainWindow()
        menuLogin = Ui_Login()
        menuLogin.setupUi(tela)
        ui.hide()
        tela.show()

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
        self.botaoFuncionarios.clicked.connect(
            lambda: self.switchToFuncionario(telaOpcoesGerente)
        )
        self.botaoClientes = QtWidgets.QPushButton(self.frame)
        self.botaoClientes.setGeometry(QtCore.QRect(30, 150, 231, 81))
        self.botaoClientes.setObjectName("botaoClientes")
        self.botaoClientes.clicked.connect(
            lambda: self.switchToClientes(telaOpcoesGerente)
        )
        self.botaoPassagens = QtWidgets.QPushButton(self.frame)
        self.botaoPassagens.setGeometry(QtCore.QRect(30, 260, 231, 81))
        self.botaoPassagens.setObjectName("botaoPassagens")
        self.botaoPassagens.clicked.connect(
            lambda: self.switchToPassagem(telaOpcoesGerente)
        )
        self.botaoVoltar = QtWidgets.QPushButton(self.frame)
        self.botaoVoltar.setGeometry(QtCore.QRect(30, 410, 231, 25))
        self.botaoVoltar.setObjectName("botaoVoltar")
        self.botaoVoltar.clicked.connect(
            lambda: self.switchVoltar(telaOpcoesGerente)
        )
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
        self.botaoVoltar.setText(_translate("telaOpcoesGerente", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    telaOpcoesGerente = QtWidgets.QMainWindow()
    ui = Ui_telaOpcoesGerente()
    ui.setupUi(telaOpcoesGerente)
    telaOpcoesGerente.show()
    sys.exit(app.exec_())
