# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaMenuFuncionario2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append("../../")
import views.recursos.recursos_rc


class Ui_telaMenuFuncionario(object):
  def setupUi(self, telaMenuFuncionario):
    telaMenuFuncionario.setObjectName("telaMenuFuncionario")
    telaMenuFuncionario.resize(751, 678)
    telaMenuFuncionario.setStyleSheet("#telaMenuFuncionario\n"
                                      "{\n"
                                      "background-image: url(:/fundos/fundo3.jpg);\n"
                                      "}\n"
                                      "\n"
                                      "#tabelaFuncionarios\n"
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
                                      "#botaoSair\n"
                                      "{\n"
                                      "font: 14pt \"Bitstream Vera Sans\";\n"
                                      "border-radius:9px;\n"
                                      "color: rgb(243, 243, 125);\n"
                                      "background-color: rgb(3, 37, 108);\n"
                                      "}\n"
                                      "#botaoSair:hover\n"
                                      "{\n"
                                      "font: 14pt \"Bitstream Vera Sans\";\n"
                                      "border-radius:9px;\n"
                                      "background-color: #6E8898;\n"
                                      "}\n"
                                      "\n"
                                      "#botaoRegistrar\n"
                                      "{\n"
                                      "font: 14pt \"Bitstream Vera Sans\";\n"
                                      "border-radius:9px;\n"
                                      "color: rgb(125, 47, 49);\n"
                                      "background-color: #9FB1BC;\n"
                                      "}\n"
                                      "#botaoRegistrar:hover\n"
                                      "{\n"
                                      "font: 14pt \"Bitstream Vera Sans\";\n"
                                      "border-radius:9px;\n"
                                      "background-color: #6E8898;\n"
                                      "}\n"
                                      "#botaoRemover\n"
                                      "{\n"
                                      "font: 14pt \"Bitstream Vera Sans\";\n"
                                      "border-radius:9px;\n"
                                      "color: rgb(125, 47, 49);\n"
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
                                      "color: rgb(125, 47, 49);\n"
                                      "background-color: #9FB1BC;\n"
                                      "}\n"
                                      "#botaoAlterar:hover\n"
                                      "{\n"
                                      "font: 14pt \"Bitstream Vera Sans\";\n"
                                      "border-radius:9px;\n"
                                      "background-color: #6E8898;\n"
                                      "}")
    self.centralwidget = QtWidgets.QWidget(telaMenuFuncionario)
    self.centralwidget.setObjectName("centralwidget")
    self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
    self.horizontalLayout_6.setObjectName("horizontalLayout_6")
    self.verticalLayout_6 = QtWidgets.QVBoxLayout()
    self.verticalLayout_6.setSizeConstraint(
        QtWidgets.QLayout.SetNoConstraint)
    self.verticalLayout_6.setContentsMargins(5, -1, 5, 5)
    self.verticalLayout_6.setObjectName("verticalLayout_6")
    self.frameListaOpcoes = QtWidgets.QFrame(self.centralwidget)
    self.frameListaOpcoes.setMinimumSize(QtCore.QSize(201, 0))
    self.frameListaOpcoes.setMaximumSize(QtCore.QSize(374, 16777215))
    self.frameListaOpcoes.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.frameListaOpcoes.setFrameShadow(QtWidgets.QFrame.Raised)
    self.frameListaOpcoes.setObjectName("frameListaOpcoes")
    self.listaOpcoes = QtWidgets.QTreeWidget(self.frameListaOpcoes)
    self.listaOpcoes.setGeometry(QtCore.QRect(10, 40, 161, 301))
    font = QtGui.QFont()
    font.setFamily("MathJax_Size1")
    font.setPointSize(15)
    font.setBold(False)
    font.setItalic(False)
    font.setWeight(50)
    self.listaOpcoes.setFont(font)
    self.listaOpcoes.setStyleSheet("")
    self.listaOpcoes.setAutoScroll(False)
    self.listaOpcoes.setEditTriggers(
        QtWidgets.QAbstractItemView.EditKeyPressed)
    self.listaOpcoes.setSelectionMode(
        QtWidgets.QAbstractItemView.SingleSelection)
    self.listaOpcoes.setIndentation(30)
    self.listaOpcoes.setUniformRowHeights(False)
    self.listaOpcoes.setAllColumnsShowFocus(False)
    self.listaOpcoes.setObjectName("listaOpcoes")
    self.listaOpcoes.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
    item_0 = QtWidgets.QTreeWidgetItem(self.listaOpcoes)
    font = QtGui.QFont()
    font.setBold(True)
    font.setWeight(75)
    item_0.setFont(0, font)
    item_1 = QtWidgets.QTreeWidgetItem(item_0)
    item_0 = QtWidgets.QTreeWidgetItem(self.listaOpcoes)
    font = QtGui.QFont()
    font.setBold(True)
    font.setWeight(75)
    item_0.setFont(0, font)
    self.listaOpcoes.header().setVisible(False)
    self.listaOpcoes.header().setCascadingSectionResizes(True)
    self.listaOpcoes.header().setMinimumSectionSize(30)
    self.verticalLayout_6.addWidget(self.frameListaOpcoes)
    self.botaoSair = QtWidgets.QPushButton(self.centralwidget)
    self.botaoSair.setMinimumSize(QtCore.QSize(201, 0))
    self.botaoSair.setMaximumSize(QtCore.QSize(374, 16777215))
    self.botaoSair.setObjectName("botaoSair")
    self.verticalLayout_6.addWidget(self.botaoSair)
    self.verticalLayout_6.setStretch(0, 1)
    self.horizontalLayout_6.addLayout(self.verticalLayout_6)
    self.verticalLayout_8 = QtWidgets.QVBoxLayout()
    self.verticalLayout_8.setContentsMargins(-1, -1, -1, 5)
    self.verticalLayout_8.setObjectName("verticalLayout_8")
    self.tabelaFuncionarios = QtWidgets.QTableWidget(self.centralwidget)
    font = QtGui.QFont()
    font.setPointSize(12)
    self.tabelaFuncionarios.setFont(font)
    self.tabelaFuncionarios.setVerticalScrollBarPolicy(
        QtCore.Qt.ScrollBarAlwaysOff)
    self.tabelaFuncionarios.setSizeAdjustPolicy(
        QtWidgets.QAbstractScrollArea.AdjustIgnored)
    self.tabelaFuncionarios.setAutoScroll(True)
    self.tabelaFuncionarios.setProperty("showDropIndicator", False)
    self.tabelaFuncionarios.setAlternatingRowColors(False)
    self.tabelaFuncionarios.setSelectionMode(
        QtWidgets.QAbstractItemView.SingleSelection)
    self.tabelaFuncionarios.setSelectionBehavior(
        QtWidgets.QAbstractItemView.SelectRows)
    self.tabelaFuncionarios.setShowGrid(True)
    self.tabelaFuncionarios.setGridStyle(QtCore.Qt.DashLine)
    self.tabelaFuncionarios.setCornerButtonEnabled(False)
    self.tabelaFuncionarios.setRowCount(9)
    self.tabelaFuncionarios.setColumnCount(6)
    self.tabelaFuncionarios.setObjectName("tabelaFuncionarios")
    self.tabelaFuncionarios.horizontalHeader().setVisible(False)
    self.tabelaFuncionarios.horizontalHeader().setDefaultSectionSize(238)
    self.tabelaFuncionarios.horizontalHeader().setStretchLastSection(False)
    self.tabelaFuncionarios.verticalHeader().setVisible(False)
    self.tabelaFuncionarios.verticalHeader().setDefaultSectionSize(60)
    self.verticalLayout_8.addWidget(self.tabelaFuncionarios)
    self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_8.setObjectName("horizontalLayout_8")
    self.botaoRegistrar = QtWidgets.QPushButton(self.centralwidget)
    self.botaoRegistrar.setObjectName("botaoRegistrar")
    self.horizontalLayout_8.addWidget(self.botaoRegistrar)
    self.botaoAlterar = QtWidgets.QPushButton(self.centralwidget)
    self.botaoAlterar.setObjectName("botaoAlterar")
    self.horizontalLayout_8.addWidget(self.botaoAlterar)
    self.botaoRemover = QtWidgets.QPushButton(self.centralwidget)
    self.botaoRemover.setObjectName("botaoRemover")
    self.horizontalLayout_8.addWidget(self.botaoRemover)
    self.verticalLayout_8.addLayout(self.horizontalLayout_8)
    self.horizontalLayout_6.addLayout(self.verticalLayout_8)
    telaMenuFuncionario.setCentralWidget(self.centralwidget)
    self.menubar = QtWidgets.QMenuBar(telaMenuFuncionario)
    self.menubar.setGeometry(QtCore.QRect(0, 0, 751, 22))
    self.menubar.setObjectName("menubar")
    telaMenuFuncionario.setMenuBar(self.menubar)

    self.retranslateUi(telaMenuFuncionario)
    QtCore.QMetaObject.connectSlotsByName(telaMenuFuncionario)

  def retranslateUi(self, telaMenuFuncionario):
    _translate = QtCore.QCoreApplication.translate
    telaMenuFuncionario.setWindowTitle(
        _translate("telaMenuFuncionario", "AirSys - Menu"))
    self.listaOpcoes.setSortingEnabled(False)
    self.listaOpcoes.headerItem().setText(
        0, _translate("telaMenuFuncionario", "Opções"))
    __sortingEnabled = self.listaOpcoes.isSortingEnabled()
    self.listaOpcoes.setSortingEnabled(False)
    self.listaOpcoes.topLevelItem(0).setText(
        0, _translate("telaMenuFuncionario", "Clientes"))
    self.listaOpcoes.topLevelItem(0).child(0).setText(
        0, _translate("telaMenuFuncionario", "Registrar"))
    self.listaOpcoes.topLevelItem(1).setText(
        0, _translate("telaMenuFuncionario", "Passagens"))
    self.listaOpcoes.setSortingEnabled(__sortingEnabled)
    self.botaoSair.setText(_translate("telaMenuFuncionario", "Sair"))
    self.botaoRegistrar.setText(_translate("telaMenuFuncionario", "Registrar"))
    self.botaoAlterar.setText(_translate("telaMenuFuncionario", "Alterar"))
    self.botaoRemover.setText(_translate("telaMenuFuncionario", "Remover"))


if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  telaMenuFuncionario = QtWidgets.QMainWindow()
  ui = Ui_telaMenuFuncionario()
  ui.setupUi(telaMenuFuncionario)
  telaMenuFuncionario.show()
  sys.exit(app.exec_())
