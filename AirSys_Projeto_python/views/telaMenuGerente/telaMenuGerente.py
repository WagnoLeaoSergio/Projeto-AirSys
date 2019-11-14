# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaMenuGerente.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

sys.path.append("../")

class Ui_telaMenuGerente(object):

    def teste(self):
        print("Clicado")

    def setupUi(self, telaMenuGerente):
        telaMenuGerente.setObjectName("telaMenuGerente")
        telaMenuGerente.resize(798, 590)
        telaMenuGerente.setStyleSheet("#telaMenuGerente\n"
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
                                      "#botaoRemover\n"
                                      "{\n"
                                      "font: 14pt \"Bitstream Vera Sans\";\n"
                                      "border-radius:9px;\n"
                                      "color: rgb(243, 223, 162);\n"
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
                                      "color: rgb(243, 223, 162);\n"
                                      "background-color: #9FB1BC;\n"
                                      "}\n"
                                      "#botaoAlterar:hover\n"
                                      "{\n"
                                      "font: 14pt \"Bitstream Vera Sans\";\n"
                                      "border-radius:9px;\n"
                                      "background-color: #6E8898;\n"
                                      "}")
        self.centralwidget = QtWidgets.QWidget(telaMenuGerente)
        self.centralwidget.setObjectName("centralwidget")
        self.tabelaFuncionarios = QtWidgets.QTableWidget(self.centralwidget)
        self.tabelaFuncionarios.setGeometry(QtCore.QRect(280, 30, 511, 471))
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
        self.tabelaFuncionarios.setShowGrid(False)
        self.tabelaFuncionarios.setGridStyle(QtCore.Qt.NoPen)
        self.tabelaFuncionarios.setCornerButtonEnabled(False)
        self.tabelaFuncionarios.setObjectName("tabelaFuncionarios")
        self.tabelaFuncionarios.setColumnCount(5)
        self.tabelaFuncionarios.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaFuncionarios.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaFuncionarios.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaFuncionarios.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaFuncionarios.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaFuncionarios.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaFuncionarios.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaFuncionarios.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaFuncionarios.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaFuncionarios.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaFuncionarios.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaFuncionarios.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaFuncionarios.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaFuncionarios.setHorizontalHeaderItem(4, item)
        self.tabelaFuncionarios.horizontalHeader().setVisible(False)
        self.tabelaFuncionarios.horizontalHeader().setDefaultSectionSize(101)
        self.tabelaFuncionarios.horizontalHeader().setStretchLastSection(False)
        self.tabelaFuncionarios.verticalHeader().setVisible(False)
        self.tabelaFuncionarios.verticalHeader().setDefaultSectionSize(60)
        self.frameListaOpcoes = QtWidgets.QFrame(self.centralwidget)
        self.frameListaOpcoes.setGeometry(QtCore.QRect(10, 30, 261, 471))
        self.frameListaOpcoes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameListaOpcoes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameListaOpcoes.setObjectName("frameListaOpcoes")
        self.listaOpcoes = QtWidgets.QTreeWidget(self.frameListaOpcoes)
        self.listaOpcoes.setGeometry(QtCore.QRect(10, 40, 241, 361))
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
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.listaOpcoes)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item_0.setFont(0, font)
        self.listaOpcoes.header().setVisible(False)
        self.listaOpcoes.header().setCascadingSectionResizes(True)
        self.listaOpcoes.header().setMinimumSectionSize(30)
        self.botaoVoltar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoVoltar.setGeometry(QtCore.QRect(10, 510, 261, 41))
        self.botaoVoltar.setObjectName("botaoVoltar")
        self.botaoRemover = QtWidgets.QPushButton(self.centralwidget)
        self.botaoRemover.setGeometry(QtCore.QRect(290, 510, 231, 41))
        self.botaoRemover.setObjectName("botaoRemover")
        self.botaoAlterar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoAlterar.setGeometry(QtCore.QRect(530, 510, 241, 41))
        self.botaoAlterar.setObjectName("botaoAlterar")
        telaMenuGerente.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(telaMenuGerente)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 22))
        self.menubar.setObjectName("menubar")
        telaMenuGerente.setMenuBar(self.menubar)

        self.retranslateUi(telaMenuGerente)
        QtCore.QMetaObject.connectSlotsByName(telaMenuGerente)

    def retranslateUi(self, telaMenuGerente):
        _translate = QtCore.QCoreApplication.translate
        telaMenuGerente.setWindowTitle(
            _translate("telaMenuGerente", "AirSys - Menu"))
        item = self.tabelaFuncionarios.verticalHeaderItem(0)
        item.setText(_translate("telaMenuGerente", "New Row"))
        item = self.tabelaFuncionarios.verticalHeaderItem(1)
        item.setText(_translate("telaMenuGerente", "New Row"))
        item = self.tabelaFuncionarios.verticalHeaderItem(2)
        item.setText(_translate("telaMenuGerente", "New Row"))
        item = self.tabelaFuncionarios.verticalHeaderItem(3)
        item.setText(_translate("telaMenuGerente", "New Row"))
        item = self.tabelaFuncionarios.verticalHeaderItem(4)
        item.setText(_translate("telaMenuGerente", "New Row"))
        item = self.tabelaFuncionarios.verticalHeaderItem(5)
        item.setText(_translate("telaMenuGerente", "New Row"))
        item = self.tabelaFuncionarios.verticalHeaderItem(6)
        item.setText(_translate("telaMenuGerente", "New Row"))
        item = self.tabelaFuncionarios.verticalHeaderItem(7)
        item.setText(_translate("telaMenuGerente", "New Row"))
        item = self.tabelaFuncionarios.horizontalHeaderItem(0)
        item.setText(_translate("telaMenuGerente", "New Column"))
        item = self.tabelaFuncionarios.horizontalHeaderItem(1)
        item.setText(_translate("telaMenuGerente", "codigo"))
        item = self.tabelaFuncionarios.horizontalHeaderItem(2)
        item.setText(_translate("telaMenuGerente", "nome"))
        item = self.tabelaFuncionarios.horizontalHeaderItem(3)
        item.setText(_translate("telaMenuGerente", "cpf"))
        item = self.tabelaFuncionarios.horizontalHeaderItem(4)
        item.setText(_translate("telaMenuGerente", "numVendas"))
        self.listaOpcoes.setSortingEnabled(False)
        self.listaOpcoes.headerItem().setText(0, _translate("telaMenuGerente", "Opções"))
        __sortingEnabled = self.listaOpcoes.isSortingEnabled()
        self.listaOpcoes.setSortingEnabled(False)
        self.listaOpcoes.topLevelItem(0).setText(
            0, _translate("telaMenuGerente", "Funcionarios"))
        self.listaOpcoes.topLevelItem(0).child(0).setText(
            0, _translate("telaMenuGerente", "Registrar"))
        self.listaOpcoes.topLevelItem(1).setText(
            0, _translate("telaMenuGerente", "Clientes"))
        self.listaOpcoes.topLevelItem(1).child(0).setText(
            0, _translate("telaMenuGerente", "Registrar"))
        self.listaOpcoes.topLevelItem(2).setText(
            0, _translate("telaMenuGerente", "Passagens"))
        self.listaOpcoes.setSortingEnabled(__sortingEnabled)
        self.listaOpcoes.itemClicked.connect(self.teste)
        self.listaOpcoes.topLevelItem.clicked.connect(self.test)
        self.botaoVoltar.setText(_translate("telaMenuGerente", "Sair"))
        self.botaoRemover.setText(_translate("telaMenuGerente", "Remover"))
        self.botaoAlterar.setText(_translate("telaMenuGerente", "Alterar"))


import recursos.recursos_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    telaMenuGerente = QtWidgets.QMainWindow()
    ui = Ui_telaMenuGerente()
    ui.setupUi(telaMenuGerente)
    telaMenuGerente.show()
    sys.exit(app.exec_())
