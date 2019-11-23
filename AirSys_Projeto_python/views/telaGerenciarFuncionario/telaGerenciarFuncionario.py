# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaGerenciarFuncionario.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append("../../")
import views.recursos.recursos_rc


class Ui_telaGerenciarFuncionario(object):
  def setupUi(self, telaGerenciarFuncionario):
    telaGerenciarFuncionario.setObjectName("telaGerenciarFuncionario")
    telaGerenciarFuncionario.resize(829, 567)
    telaGerenciarFuncionario.setStyleSheet("#telaGerenciarFuncionario\n"
                                           "{\n"
                                           "background-image: url(:/fundos/fundo3.jpg);\n"
                                           "}\n"
                                           "\n"
                                           "#tabelaFuncionario\n"
                                           "{\n"
                                           "border-radius: 10px;\n"
                                           "background-color: rgba(239, 230, 221, 150);\n"
                                           "}\n"
                                           "\n"
                                           "#frameListaOpcoes\n"
                                           "{\n"
                                           "border-radius: 10px;\n"
                                           "background-color: rgba(239, 230, 221, 150);\n"
                                           "}\n"
                                           "\n"
                                           "#listaOpcoes\n"
                                           "{\n"
                                           "font: 15pt \"MathJax_Size1\";\n"
                                           "background-color: rgb(255, 255, 255, 0);\n"
                                           "}\n"
                                           "\n"
                                           "#botaoVoltar\n"
                                           "{\n"
                                           "font: 14pt \"Bitstream Vera Sans\";\n"
                                           "border-radius:9px;\n"
                                           "color: rgb(243, 223, 162);\n"
                                           "background-color: rgb(3, 37, 108);\n"
                                           "}\n"
                                           "#botaoVoltar:hover\n"
                                           "{\n"
                                           "font: 14pt \"Bitstream Vera Sans\";\n"
                                           "border-radius:9px;\n"
                                           "background-color: #6E8898;\n"
                                           "}\n"
                                           "\n"
                                           "#botaoInserir\n"
                                           "{\n"
                                           "font: 14pt \"Bitstream Vera Sans\";\n"
                                           "border-radius:9px;\n"
                                           "color: rgb(3, 37, 108);\n"
                                           "background-color: #9FB1BC;\n"
                                           "}\n"
                                           "#botaoInserir:hover\n"
                                           "{\n"
                                           "font: 14pt \"Bitstream Vera Sans\";\n"
                                           "border-radius:9px;\n"
                                           "background-color: #6E8898;\n"
                                           "}\n"
                                           "\n"
                                           "\n"
                                           "#botaoRemover\n"
                                           "{\n"
                                           "font: 14pt \"Bitstream Vera Sans\";\n"
                                           "border-radius:9px;\n"
                                           "color: rgb(3, 37, 108);\n"
                                           "background-color: #9FB1BC;\n"
                                           "}\n"
                                           "#botaoRemover:hover\n"
                                           "{\n"
                                           "font: 14pt \"Bitstream Vera Sans\";\n"
                                           "border-radius:9px;\n"
                                           "background-color: #6E8898;\n"
                                           "}\n"
                                           "\n"
                                           "#botaoAlterar\n"
                                           "{\n"
                                           "font: 14pt \"Bitstream Vera Sans\";\n"
                                           "border-radius:9px;\n"
                                           "color: rgb(3, 37, 108);\n"
                                           "background-color: #9FB1BC;\n"
                                           "}\n"
                                           "#botaoAlterar:hover\n"
                                           "{\n"
                                           "font: 14pt \"Bitstream Vera Sans\";\n"
                                           "border-radius:9px;\n"
                                           "background-color: #6E8898;\n"
                                           "}")
    self.centralwidget = QtWidgets.QWidget(telaGerenciarFuncionario)
    self.centralwidget.setObjectName("centralwidget")
    self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
    self.gridLayout.setObjectName("gridLayout")
    self.verticalLayout = QtWidgets.QVBoxLayout()
    self.verticalLayout.setObjectName("verticalLayout")
    self.tabelaFuncionario = QtWidgets.QTableWidget(self.centralwidget)
    font = QtGui.QFont()
    font.setPointSize(12)
    self.tabelaFuncionario.setFont(font)
    self.tabelaFuncionario.setVerticalScrollBarPolicy(
        QtCore.Qt.ScrollBarAlwaysOff)
    self.tabelaFuncionario.setSizeAdjustPolicy(
        QtWidgets.QAbstractScrollArea.AdjustIgnored)
    self.tabelaFuncionario.setAutoScroll(True)
    self.tabelaFuncionario.setProperty("showDropIndicator", False)
    self.tabelaFuncionario.setAlternatingRowColors(False)
    self.tabelaFuncionario.setSelectionMode(
        QtWidgets.QAbstractItemView.SingleSelection)
    self.tabelaFuncionario.setSelectionBehavior(
        QtWidgets.QAbstractItemView.SelectRows)
    self.tabelaFuncionario.setShowGrid(True)
    self.tabelaFuncionario.setGridStyle(QtCore.Qt.SolidLine)
    self.tabelaFuncionario.setCornerButtonEnabled(False)
    self.tabelaFuncionario.setRowCount(13)
    self.tabelaFuncionario.setObjectName("tabelaFuncionario")
    self.tabelaFuncionario.setColumnCount(5)
    item = QtWidgets.QTableWidgetItem()
    self.tabelaFuncionario.setVerticalHeaderItem(0, item)
    item = QtWidgets.QTableWidgetItem()
    self.tabelaFuncionario.setVerticalHeaderItem(1, item)
    item = QtWidgets.QTableWidgetItem()
    self.tabelaFuncionario.setVerticalHeaderItem(2, item)
    item = QtWidgets.QTableWidgetItem()
    self.tabelaFuncionario.setVerticalHeaderItem(3, item)
    item = QtWidgets.QTableWidgetItem()
    self.tabelaFuncionario.setVerticalHeaderItem(4, item)
    item = QtWidgets.QTableWidgetItem()
    self.tabelaFuncionario.setVerticalHeaderItem(5, item)
    item = QtWidgets.QTableWidgetItem()
    self.tabelaFuncionario.setVerticalHeaderItem(6, item)
    item = QtWidgets.QTableWidgetItem()
    self.tabelaFuncionario.setVerticalHeaderItem(7, item)
    item = QtWidgets.QTableWidgetItem()
    self.tabelaFuncionario.setHorizontalHeaderItem(0, item)
    item = QtWidgets.QTableWidgetItem()
    self.tabelaFuncionario.setHorizontalHeaderItem(1, item)
    item = QtWidgets.QTableWidgetItem()
    self.tabelaFuncionario.setHorizontalHeaderItem(2, item)
    item = QtWidgets.QTableWidgetItem()
    self.tabelaFuncionario.setHorizontalHeaderItem(3, item)
    item = QtWidgets.QTableWidgetItem()
    self.tabelaFuncionario.setHorizontalHeaderItem(4, item)
    self.tabelaFuncionario.horizontalHeader().setVisible(False)
    self.tabelaFuncionario.horizontalHeader().setDefaultSectionSize(161)
    self.tabelaFuncionario.horizontalHeader().setStretchLastSection(False)
    self.tabelaFuncionario.verticalHeader().setVisible(False)
    self.tabelaFuncionario.verticalHeader().setDefaultSectionSize(65)
    self.verticalLayout.addWidget(self.tabelaFuncionario)
    self.horizontalLayout = QtWidgets.QHBoxLayout()
    self.horizontalLayout.setObjectName("horizontalLayout")
    self.botaoInserir = QtWidgets.QPushButton(self.centralwidget)
    self.botaoInserir.setObjectName("botaoInserir")
    self.horizontalLayout.addWidget(self.botaoInserir)
    self.botaoRemover = QtWidgets.QPushButton(self.centralwidget)
    self.botaoRemover.setObjectName("botaoRemover")
    self.horizontalLayout.addWidget(self.botaoRemover)
    self.botaoAlterar = QtWidgets.QPushButton(self.centralwidget)
    self.botaoAlterar.setObjectName("botaoAlterar")
    self.horizontalLayout.addWidget(self.botaoAlterar)
    self.botaoVoltar = QtWidgets.QPushButton(self.centralwidget)
    self.botaoVoltar.setObjectName("botaoVoltar")
    self.horizontalLayout.addWidget(self.botaoVoltar)
    self.verticalLayout.addLayout(self.horizontalLayout)
    self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
    telaGerenciarFuncionario.setCentralWidget(self.centralwidget)

    self.retranslateUi(telaGerenciarFuncionario)
    QtCore.QMetaObject.connectSlotsByName(telaGerenciarFuncionario)

  def retranslateUi(self, telaGerenciarFuncionario):
    _translate = QtCore.QCoreApplication.translate
    telaGerenciarFuncionario.setWindowTitle(
        _translate("telaGerenciarFuncionario", "AirSys - Menu"))
    item = self.tabelaFuncionario.verticalHeaderItem(0)
    item.setText(_translate("telaGerenciarFuncionario", "New Row"))
    item = self.tabelaFuncionario.verticalHeaderItem(1)
    item.setText(_translate("telaGerenciarFuncionario", "New Row"))
    item = self.tabelaFuncionario.verticalHeaderItem(2)
    item.setText(_translate("telaGerenciarFuncionario", "New Row"))
    item = self.tabelaFuncionario.verticalHeaderItem(3)
    item.setText(_translate("telaGerenciarFuncionario", "New Row"))
    item = self.tabelaFuncionario.verticalHeaderItem(4)
    item.setText(_translate("telaGerenciarFuncionario", "New Row"))
    item = self.tabelaFuncionario.verticalHeaderItem(5)
    item.setText(_translate("telaGerenciarFuncionario", "New Row"))
    item = self.tabelaFuncionario.verticalHeaderItem(6)
    item.setText(_translate("telaGerenciarFuncionario", "New Row"))
    item = self.tabelaFuncionario.verticalHeaderItem(7)
    item.setText(_translate("telaGerenciarFuncionario", "New Row"))
    item = self.tabelaFuncionario.horizontalHeaderItem(0)
    item.setText(_translate("telaGerenciarFuncionario", "New Column"))
    item = self.tabelaFuncionario.horizontalHeaderItem(1)
    item.setText(_translate("telaGerenciarFuncionario", "codigo"))
    item = self.tabelaFuncionario.horizontalHeaderItem(2)
    item.setText(_translate("telaGerenciarFuncionario", "nome"))
    item = self.tabelaFuncionario.horizontalHeaderItem(3)
    item.setText(_translate("telaGerenciarFuncionario", "cpf"))
    item = self.tabelaFuncionario.horizontalHeaderItem(4)
    item.setText(_translate("telaGerenciarFuncionario", "numVendas"))
    self.botaoInserir.setText(_translate(
        "telaGerenciarFuncionario", "Inserir"))
    self.botaoRemover.setText(_translate(
        "telaGerenciarFuncionario", "Remover"))
    self.botaoAlterar.setText(_translate(
        "telaGerenciarFuncionario", "Alterar"))
    self.botaoVoltar.setText(_translate(
        "telaGerenciarFuncionario", "Sair"))


if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  telaGerenciarFuncionario = QtWidgets.QMainWindow()
  ui = Ui_telaGerenciarFuncionario()
  ui.setupUi(telaGerenciarFuncionario)
  telaGerenciarFuncionario.show()
  sys.exit(app.exec_())
