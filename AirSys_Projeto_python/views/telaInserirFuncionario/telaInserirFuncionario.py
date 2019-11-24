# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaInserirFuncionario.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append("../../")
import views.recursos.recursos_rc


class Ui_telaInserirFuncionario(object):
    def __init__(self, gerenciarObj):
        self.gerenciarObj = gerenciarObj

    def registrar(self):
        import controles
        fList = controles.ListaFuncionarios()
        novo_funcionario = controles.Funcionario()
        cod = self.campoCodigo.text()
        if cod == "":
            print("Por favor insira um codigo para o funcionario")
            return
        busca = fList.buscarFuncionario(cod)
        if busca is not None:
            print("Funcionario com codigo ja cadastrado")
            return

        nome = self.campoNome.text()
        numId = self.campoID.text()
        cpf = self.campoCPF.text()
        email = self.campoEmail.text()
        campoSenha = self.campoSenha.text()
        novo_funcionario.setCodigo(cod)
        novo_funcionario.setNome(nome)
        novo_funcionario.setNumIdetidade(numId)
        novo_funcionario.setCPF(cpf)
        novo_funcionario.setEmail(email)
        novo_funcionario.setSenha(campoSenha)
        msg = fList.registrarFuncionario(codigo=cod, funcionario=novo_funcionario)
        print(msg)
        self.gerenciarObj.updateTable()

    def setupUi(self, telaInserirFuncionario):
        telaInserirFuncionario.setObjectName("telaInserirFuncionario")
        telaInserirFuncionario.resize(407, 538)
        telaInserirFuncionario.setMinimumSize(QtCore.QSize(407, 538))
        telaInserirFuncionario.setMaximumSize(QtCore.QSize(407, 538))
        telaInserirFuncionario.setStyleSheet("#telaInserirFuncionario\n"
                                             "{\n"
                                             "background-image: url(:/fundos/fundo3.jpg);\n"
                                             "}\n"
                                             "#frameDados\n"
                                             "{\n"
                                             "background-color: rgba(13, 125, 159, 80);\n"
                                             "}\n"
                                             "#labelInfo\n"
                                             "{\n"
                                             "font: 13pt \"Noto Serif Malayalam\";\n"
                                             "color: rgb(243, 234, 225);\n"
                                             "}\n"
                                             "\n"
                                             "#campoCodigo\n"
                                             "{\n"
                                             "color: rgb(243, 234, 225);\n"
                                             "background-color: rgba(37, 128, 197, 150);\n"
                                             "}\n"
                                             "\n"
                                             "#campoNome\n"
                                             "{\n"
                                             "color: rgb(243, 234, 225);\n"
                                             "background-color: rgba(37, 128, 197, 150);\n"
                                             "}\n"
                                             "\n"
                                             "#campoID\n"
                                             "{\n"
                                             "color: rgb(243, 234, 225);\n"
                                             "background-color: rgba(37, 128, 197, 150);\n"
                                             "}\n"
                                             "\n"
                                             "#campoCPF\n"
                                             "{\n"
                                             "color: rgb(243, 234, 225);\n"
                                             "background-color: rgba(37, 128, 197, 150);\n"
                                             "}\n"
                                             "\n"
                                             "#campoEmail\n"
                                             "{\n"
                                             "color: rgb(243, 234, 225);\n"
                                             "background-color: rgba(37, 128, 197, 150);\n"
                                             "}\n"
                                             "\n"
                                             "#campoSenha\n"
                                             "{\n"
                                             "color: rgb(243, 234, 225);\n"
                                             "background-color: rgba(37, 128, 197, 150);\n"
                                             "}\n"
                                             "\n"
                                             "#botaoSubmeter\n"
                                             "{\n"
                                             "color: rgb(8, 76, 97);\n"
                                             "font: 12pt \"Noto Serif Malayalam\";\n"
                                             "border-radius:5px;\n"
                                             "background-color: rgb(238, 219, 159);\n"
                                             "}\n"
                                             "#botaoSubmeter:hover\n"
                                             "{\n"
                                             "color: rgb(8, 76, 97);\n"
                                             "font: 12pt \"Noto Serif Malayalam\";\n"
                                             "border-radius:5px;\n"
                                             "background-color: rgb(194, 178, 129);\n"
                                             "}")
        self.centralwidget = QtWidgets.QWidget(telaInserirFuncionario)
        self.centralwidget.setObjectName("centralwidget")
        self.frameDados = QtWidgets.QFrame(self.centralwidget)
        self.frameDados.setGeometry(QtCore.QRect(40, 30, 331, 461))
        self.frameDados.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameDados.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameDados.setObjectName("frameDados")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frameDados)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 60, 231, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.campoCodigo = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.campoCodigo.setObjectName("campoCodigo")
        self.verticalLayout.addWidget(self.campoCodigo)
        self.campoNome = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.campoNome.setObjectName("campoNome")
        self.verticalLayout.addWidget(self.campoNome)
        self.campoID = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.campoID.setObjectName("campoID")
        self.verticalLayout.addWidget(self.campoID)
        self.campoCPF = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.campoCPF.setObjectName("campoCPF")
        self.verticalLayout.addWidget(self.campoCPF)
        self.campoEmail = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.campoEmail.setObjectName("campoEmail")
        self.verticalLayout.addWidget(self.campoEmail)
        self.campoSenha = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.campoSenha.setObjectName("campoSenha")
        self.verticalLayout.addWidget(self.campoSenha)
        self.labelInfo = QtWidgets.QLabel(self.frameDados)
        self.labelInfo.setGeometry(QtCore.QRect(0, 20, 331, 31))
        self.labelInfo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInfo.setObjectName("labelInfo")
        self.botaoSubmeter = QtWidgets.QPushButton(self.centralwidget)
        self.botaoSubmeter.setGeometry(QtCore.QRect(140, 500, 121, 31))
        self.botaoSubmeter.setObjectName("botaoSubmeter")
        self.botaoSubmeter.clicked.connect(self.registrar)
        telaInserirFuncionario.setCentralWidget(self.centralwidget)

        self.retranslateUi(telaInserirFuncionario)
        QtCore.QMetaObject.connectSlotsByName(telaInserirFuncionario)

    def retranslateUi(self, telaInserirFuncionario):
        _translate = QtCore.QCoreApplication.translate
        telaInserirFuncionario.setWindowTitle(
            _translate("telaInserirFuncionario", "Inseir Funcionario"))
        self.campoCodigo.setPlaceholderText(
            _translate("telaInserirFuncionario", "CODIGO"))
        self.campoNome.setPlaceholderText(
            _translate("telaInserirFuncionario", "NOME"))
        self.campoID.setPlaceholderText(_translate(
            "telaInserirFuncionario", "Nº DE IDENTIDADE"))
        self.campoCPF.setPlaceholderText(
            _translate("telaInserirFuncionario", "CPF"))
        self.campoEmail.setPlaceholderText(
            _translate("telaInserirFuncionario", "EMAIL"))
        self.campoSenha.setPlaceholderText(
            _translate("telaInserirFuncionario", "SENHA"))
        self.labelInfo.setText(_translate(
            "telaInserirFuncionario", "Insira aqui os dados do funcionário"))
        self.botaoSubmeter.setText(_translate(
            "telaInserirFuncionario", "Submeter"))

"""
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    telaInserirFuncionario = QtWidgets.QMainWindow()
    ui = Ui_telaInserirFuncionario()
    ui.setupUi(telaInserirFuncionario)
    telaInserirFuncionario.show()
    sys.exit(app.exec_())
"""