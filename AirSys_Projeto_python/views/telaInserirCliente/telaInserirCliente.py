# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaInserirCliente.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append("../../")
import views.recursos.recursos_rc
import controles

class Ui_telaInserirCliente(object):
    def __init__(self, gerenciarObj):
        self.gerenciarObj = gerenciarObj

    def registrar(self):
        import controles
        cList = controles.ListaClientes()
        novo_cliente = controles.Cliente()
        cod = self.campoCodigo.text()
        if cod == "":
            print("Por favor insira um codigo para o cliente")
            return
        busca = cList.buscarCliente(cod)
        if busca is not None:
            print("Cliente com codigo ja cadastrado")
            return

        nome = self.campoNome.text()
        numId = self.campoID.text()
        cpf = self.campoCPF.text()
        email = self.campoEmail.text()
        banco = self.campoBanco.text()
        novo_cliente.setCodigo(cod)
        novo_cliente.setNome(nome)
        novo_cliente.setNumIdetidade(numId)
        novo_cliente.setCPF(cpf)
        novo_cliente.setEmail(email)
        novo_cliente.setBanco(banco)
        msg = cList.registrarCliente(codigo=cod, cliente=novo_cliente)
        print(msg)
        self.gerenciarObj.updateTable()

    def setupUi(self, telaInserirCliente):
        telaInserirCliente.setObjectName("telaInserirCliente")
        telaInserirCliente.resize(407, 538)
        telaInserirCliente.setMinimumSize(QtCore.QSize(407, 538))
        telaInserirCliente.setMaximumSize(QtCore.QSize(407, 538))
        telaInserirCliente.setStyleSheet("#telaInserirCliente\n"
                                         "{\n"
                                         "background-image: url(:/fundos/fundo3.jpg);\n"
                                         "}\n"
                                         "#frameDados\n"
                                         "{\n"
                                         "background-color: rgba(13, 125, 159, 80);\n"
                                         "}\n"
                                         "#labelInfo\n"
                                         "{\n"
                                         "font: 14pt \"Noto Serif Malayalam\";\n"
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
                                         "#campoBanco\n"
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
        self.centralwidget = QtWidgets.QWidget(telaInserirCliente)
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
        self.campoBanco = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.campoBanco.setObjectName("campoBanco")
        self.verticalLayout.addWidget(self.campoBanco)
        self.labelInfo = QtWidgets.QLabel(self.frameDados)
        self.labelInfo.setGeometry(QtCore.QRect(20, 20, 291, 31))
        self.labelInfo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInfo.setObjectName("labelInfo")
        self.botaoSubmeter = QtWidgets.QPushButton(self.centralwidget)
        self.botaoSubmeter.setGeometry(QtCore.QRect(140, 500, 121, 31))
        self.botaoSubmeter.setObjectName("botaoSubmeter")
        self.botaoSubmeter.clicked.connect(self.registrar)
        telaInserirCliente.setCentralWidget(self.centralwidget)

        self.retranslateUi(telaInserirCliente)
        QtCore.QMetaObject.connectSlotsByName(telaInserirCliente)

    def retranslateUi(self, telaInserirCliente):
        _translate = QtCore.QCoreApplication.translate
        telaInserirCliente.setWindowTitle(
            _translate("telaInserirCliente", "Inserir Cliente"))
        self.campoCodigo.setPlaceholderText(
            _translate("telaInserirCliente", "CODIGO"))
        self.campoNome.setPlaceholderText(
            _translate("telaInserirCliente", "NOME"))
        self.campoID.setPlaceholderText(_translate(
            "telaInserirCliente", "Nº DE IDENTIDADE"))
        self.campoCPF.setPlaceholderText(
            _translate("telaInserirCliente", "CPF"))
        self.campoEmail.setPlaceholderText(
            _translate("telaInserirCliente", "EMAIL"))
        self.campoBanco.setPlaceholderText(
            _translate("telaInserirCliente", "BANCO"))
        self.labelInfo.setText(_translate(
            "telaInserirCliente", "Insira aqui os dados do cliente"))
        self.botaoSubmeter.setText(_translate(
            "telaInserirCliente", "Submeter"))

"""
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    telaInserirCliente = QtWidgets.QMainWindow()
    ui = Ui_telaInserirCliente()
    ui.setupUi(telaInserirCliente)
    telaInserirCliente.show()
    sys.exit(app.exec_())
"""