# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaAlterarCliente.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

sys.path.append("../../")
import views.recursos.recursos_rc


class Ui_telaAlterarCliente:
  def __init__(self, objGerenciar, codCliente):
    self.objGerenciar = objGerenciar
    self.codCliente = codCliente

  def alterar(self):
    import controles
    cList = controles.ListaClientes()
    opcao = str(self.comboBoxOpcoes.currentText())
    novo_valor = self.campoNovoValor.text()
    if novo_valor == "":
        print("Por favor digite um valor valido")
        return
    status = cList.alterarCliente(
              codigo=self.codCliente,
              campo=opcao,
              valor=novo_valor
            )
    # print(status)
    self.objGerenciar.updateTable()

  def setupUi(self, telaAlterarCliente):
    telaAlterarCliente.setObjectName("telaAlterarCliente")
    telaAlterarCliente.resize(449, 326)
    telaAlterarCliente.setMinimumSize(QtCore.QSize(449, 326))
    telaAlterarCliente.setMaximumSize(QtCore.QSize(449, 326))
    telaAlterarCliente.setStyleSheet("#telaAlterarCliente\n"
                                      "{\n"
                                      "background-image: url(:/fundos/fundo3.jpg);\n"
                                      "}\n"
                                      "#label\n"
                                      "{\n"
                                      "color: rgb(247, 238, 229);\n"
                                      "font: 11pt \"Noto Serif Malayalam\";\n"
                                      "}\n"
                                      "\n"
                                      "#comboBoxOpcoes\n"
                                      "{\n"
                                      "font: 11pt \"Noto Serif Malayalam\";\n"
                                      "background-color: rgba(201, 201, 238, 100);\n"
                                      "}\n"
                                      "\n"
                                      "#label_2\n"
                                      "{\n"
                                      "color: rgb(247, 238, 229);\n"
                                      "font: 11pt \"Noto Serif Malayalam\";\n"
                                      "}\n"
                                      "#campoNovoValor\n"
                                      "{\n"
                                      "font: 10pt \"Noto Serif Malayalam\";\n"
                                      "background-color: rgba(201, 201, 238, 100);\n"
                                      "}\n"
                                      "\n"
                                      "#botaoAlterar\n"
                                      "{\n"
                                      "border-radius:5px;\n"
                                      "background-color: rgb(44, 134, 230);\n"
                                      "font: 11pt \"Noto Serif Malayalam\";\n"
                                      "}\n"
                                      "#botaoAlterar:hover\n"
                                      "{\n"
                                      "border-radius:5px;\n"
                                      "background-color: rgb(140, 236, 241);\n"
                                      "font: 11pt \"Noto Serif Malayalam\";\n"
                                      "}")
    self.centralwidget = QtWidgets.QWidget(telaAlterarCliente)
    self.centralwidget.setObjectName("centralwidget")
    self.botaoAlterar = QtWidgets.QPushButton(self.centralwidget)
    self.botaoAlterar.setGeometry(QtCore.QRect(150, 250, 161, 51))
    self.botaoAlterar.setObjectName("botaoAlterar")
    self.botaoAlterar.clicked.connect(self.alterar)
    self.campoNovoValor = QtWidgets.QLineEdit(self.centralwidget)
    self.campoNovoValor.setGeometry(QtCore.QRect(80, 190, 281, 31))
    self.campoNovoValor.setObjectName("campoNovoValor")
    self.comboBoxOpcoes = QtWidgets.QComboBox(self.centralwidget)
    self.comboBoxOpcoes.setGeometry(QtCore.QRect(80, 100, 281, 31))
    self.comboBoxOpcoes.setObjectName("comboBoxOpcoes")
    self.comboBoxOpcoes.addItem("")
    self.comboBoxOpcoes.addItem("")
    self.comboBoxOpcoes.addItem("")
    self.comboBoxOpcoes.addItem("")
    self.comboBoxOpcoes.addItem("")
    self.label = QtWidgets.QLabel(self.centralwidget)
    self.label.setGeometry(QtCore.QRect(80, 70, 281, 16))
    self.label.setObjectName("label")
    self.label_2 = QtWidgets.QLabel(self.centralwidget)
    self.label_2.setGeometry(QtCore.QRect(80, 160, 271, 17))
    self.label_2.setObjectName("label_2")
    telaAlterarCliente.setCentralWidget(self.centralwidget)

    self.retranslateUi(telaAlterarCliente)
    QtCore.QMetaObject.connectSlotsByName(telaAlterarCliente)

  def retranslateUi(self, telaAlterarCliente):
    _translate = QtCore.QCoreApplication.translate
    telaAlterarCliente.setWindowTitle(_translate(
        "telaAlterarCliente", "Alterar Cliente"))
    self.botaoAlterar.setText(_translate("telaAlterarCliente", "Alterar"))
    self.campoNovoValor.setPlaceholderText(
        _translate("telaAlterarCliente", "Novo valor"))
    self.comboBoxOpcoes.setItemText(
        0, _translate("telaAlterarCliente", "nome"))
    self.comboBoxOpcoes.setItemText(1, _translate(
        "telaAlterarCliente", "numIdentidade"))
    self.comboBoxOpcoes.setItemText(
        2, _translate("telaAlterarCliente", "cpf"))
    self.comboBoxOpcoes.setItemText(
        3, _translate("telaAlterarCliente", "email"))
    self.comboBoxOpcoes.setItemText(
        4, _translate("telaAlterarCliente", "banco"))
    self.label.setText(_translate("telaAlterarCliente",
                                  "Escolha o campo a ser alterado:"))
    self.label_2.setText(_translate(
        "telaAlterarCliente", "Digite o novo valor do campo:"))


"""
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    telaAlterarCliente = QtWidgets.QMainWindow()
    ui = Ui_telaAlterarCliente()
    ui.setupUi(telaAlterarCliente)
    telaAlterarCliente.show()
    sys.exit(app.exec_())
"""
