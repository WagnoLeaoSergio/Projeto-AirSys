# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaAlterarFuncionario.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

sys.path.append("../../")
import views.recursos.recursos_rc
import controles


class Ui_telaAlterarFuncionario(object):
  def __init__(self, objGerenciar, codFuncionario):
    self.objGerenciar = objGerenciar
    self.codFuncionario = codFuncionario

  def alterar(self):
    import controles
    cList = controles.ListaFuncionarios()
    opcao = str(self.comboBoxOpcoes.currentText())
    novo_valor = self.campoNovoValor.text()
    if novo_valor == "":
        print("Por favor digite um valor valido")
        return
    status = cList.alterarFuncionario(
              codigo=self.codFuncionario,
              campo=opcao,
              valor=novo_valor
            )
    # print(status)
    self.objGerenciar.updateTable()

  def setupUi(self, telaAlterarFuncionario):
    telaAlterarFuncionario.setObjectName("telaAlterarFuncionario")
    telaAlterarFuncionario.resize(449, 326)
    telaAlterarFuncionario.setMinimumSize(QtCore.QSize(449, 326))
    telaAlterarFuncionario.setMaximumSize(QtCore.QSize(449, 326))
    telaAlterarFuncionario.setStyleSheet("#telaAlterarFuncionario\n"
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
    self.centralwidget = QtWidgets.QWidget(telaAlterarFuncionario)
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
    telaAlterarFuncionario.setCentralWidget(self.centralwidget)

    self.retranslateUi(telaAlterarFuncionario)
    QtCore.QMetaObject.connectSlotsByName(telaAlterarFuncionario)

  def retranslateUi(self, telaAlterarFuncionario):
    _translate = QtCore.QCoreApplication.translate
    telaAlterarFuncionario.setWindowTitle(_translate(
        "telaAlterarFuncionario", "Alterar Funcionario"))
    self.botaoAlterar.setText(_translate("telaAlterarFuncionario", "Alterar"))
    self.campoNovoValor.setPlaceholderText(
        _translate("telaAlterarFuncionario", "Novo valor"))
    self.comboBoxOpcoes.setItemText(
        0, _translate("telaAlterarFuncionario", "nome"))
    self.comboBoxOpcoes.setItemText(1, _translate(
        "telaAlterarFuncionario", "numIdentidade"))
    self.comboBoxOpcoes.setItemText(
        2, _translate("telaAlterarFuncionario", "cpf"))
    self.comboBoxOpcoes.setItemText(
        3, _translate("telaAlterarFuncionario", "email"))
    self.comboBoxOpcoes.setItemText(
        4, _translate("telaAlterarFuncionario", "senha"))
    self.label.setText(_translate("telaAlterarFuncionario",
                                  "Escolha o campo a ser alterado:"))
    self.label_2.setText(_translate(
        "telaAlterarFuncionario", "Digite o novo valor do campo:"))


"""
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    telaAlterarFuncionario = QtWidgets.QMainWindow()
    ui = Ui_telaAlterarFuncionario()
    ui.setupUi(telaAlterarFuncionario)
    telaAlterarFuncionario.show()
    sys.exit(app.exec_())
"""
