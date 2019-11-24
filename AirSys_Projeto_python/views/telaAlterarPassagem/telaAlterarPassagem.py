# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaAlterarPassagem.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

sys.path.append("../../")
import views.recursos.recursos_rc
import controles


class Ui_telaAlterarPassagem(object):
  def __init__(self, objGerenciar, codPassagem):
    self.objGerenciar = objGerenciar
    self.codPassagem = codPassagem

  def alterar(self):
    import controles
    cList = controles.ListaPassagens()
    opcao = str(self.comboBoxOpcoes.currentText())
    novo_valor = self.campoNovoValor.text()
    if novo_valor == "":
      print("Por favor digite um valor valido")
      return
    status = cList.alterarPassagem(
        codigo=self.codPassagem,
        campo=opcao,
        valor=novo_valor
    )
    # print(status)
    self.objGerenciar.updateTable()

  def setupUi(self, telaAlterarPassagem):
    telaAlterarPassagem.setObjectName("telaAlterarPassagem")
    telaAlterarPassagem.resize(449, 326)
    telaAlterarPassagem.setMinimumSize(QtCore.QSize(449, 326))
    telaAlterarPassagem.setMaximumSize(QtCore.QSize(449, 326))
    telaAlterarPassagem.setStyleSheet("#telaAlterarPassagem\n"
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
    self.centralwidget = QtWidgets.QWidget(telaAlterarPassagem)
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
    self.comboBoxOpcoes.addItem("")
    self.label = QtWidgets.QLabel(self.centralwidget)
    self.label.setGeometry(QtCore.QRect(80, 70, 281, 16))
    self.label.setObjectName("label")
    self.label_2 = QtWidgets.QLabel(self.centralwidget)
    self.label_2.setGeometry(QtCore.QRect(80, 160, 271, 17))
    self.label_2.setObjectName("label_2")
    telaAlterarPassagem.setCentralWidget(self.centralwidget)

    self.retranslateUi(telaAlterarPassagem)
    QtCore.QMetaObject.connectSlotsByName(telaAlterarPassagem)

  def retranslateUi(self, telaAlterarPassagem):
    _translate = QtCore.QCoreApplication.translate
    telaAlterarPassagem.setWindowTitle(
        _translate("telaAlterarPassagem", "MainWindow"))
    self.botaoAlterar.setText(_translate("telaAlterarPassagem", "Alterar"))
    self.campoNovoValor.setPlaceholderText(
        _translate("telaAlterarPassagem", "Novo valor"))
    self.comboBoxOpcoes.setItemText(
        0, _translate("telaAlterarPassagem", "origem"))
    self.comboBoxOpcoes.setItemText(
        1, _translate("telaAlterarPassagem", "destino"))
    self.comboBoxOpcoes.setItemText(
        2, _translate("telaAlterarPassagem", "data"))
    self.comboBoxOpcoes.setItemText(
        3, _translate("telaAlterarPassagem", "preco"))
    self.comboBoxOpcoes.setItemText(
        4, _translate("telaAlterarPassagem", "companhia"))
    self.comboBoxOpcoes.setItemText(
        5, _translate("telaAlterarPassagem", "assento"))
    self.label.setText(_translate("telaAlterarPassagem",
                                  "Escolha o campo a ser alterado:"))
    self.label_2.setText(_translate(
        "telaAlterarPassagem", "Digite o novo valor do campo:"))


"""
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    telaAlterarPassagem = QtWidgets.QMainWindow()
    ui = Ui_telaAlterarPassagem()
    ui.setupUi(telaAlterarPassagem)
    telaAlterarPassagem.show()
    sys.exit(app.exec_())
"""
