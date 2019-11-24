# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaGerenciarFuncionario.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
sys.path.append("../../")
import views.recursos.recursos_rc
import controles

class Ui_telaGerenciarFuncionario(object):
    def __init__(self):
        self.fList = controles.ListaFuncionarios()

    def updateTable(self):
        self.cData = self.fList.listarFuncionarios()
        self.numRows = len(self.cData)
        self.numColumns = 6
        self.tabelaFuncionario.setRowCount(self.numRows)
        self.tabelaFuncionario.setColumnCount(self.numColumns)
        j = 0
        data = []
        for i in self.cData:
            passData = i["element{0}".format(j)]
            del passData["_id"]
            data.append((passData["codigo"],
                         passData["nome"],
                         passData["numIdentidade"],
                         str(passData["cpf"]),
                         passData["email"],
                         passData["senha"],
                         ))
            j = j + 1
        for row in range(self.numRows):
            for column in range(self.numColumns):
                self.tabelaFuncionario.setItem(
                    row, column, QTableWidgetItem((data[row][column]))
                )

    def remover(self):
        # encotrar indice da linha selecionada:
        # indexes = self.tabelaFuncionario.selectionModel().selectedRows()
        # remvIndex = indexes[0].row()
        cod = self.tabelaFuncionario.item(self.tabelaFuncionario.currentRow(), 0).text()
        self.fList.removerFuncionario(cod)
        self.updateTable()

    def switchToRegistrar(self, ui):
        from views.telaInserirFuncionario.telaInserirFuncionario import Ui_telaInserirFuncionario
        self.tela = QtWidgets.QMainWindow()
        self.registrar = Ui_telaInserirFuncionario(self)
        self.registrar.setupUi(self.tela)
        self.tela.show()

    def switchToAlterar(self, ui):
        from views.telaAlterarFuncionario.telaAlterarFuncionario import Ui_telaAlterarFuncionario
        cod = self.tabelaFuncionario.item(self.tabelaFuncionario.currentRow(), 0).text()
        self.tela = QtWidgets.QMainWindow()
        self.alterar = Ui_telaAlterarFuncionario(self, cod)
        self.alterar.setupUi(self.tela)
        self.tela.show()
        self.updateTable()


    def switchSair(self, ui):
            from views.telaMenuGerente.telaMenuGerente import Ui_telaOpcoesGerente
            self.tela = QtWidgets.QMainWindow()
            self.menuGerente = Ui_telaOpcoesGerente()
            self.menuGerente.setupUi(self.tela)
            ui.hide()
            self.tela.show()

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
                                             "#botaoSair\n"
                                             "{\n"
                                             "font: 14pt \"Bitstream Vera Sans\";\n"
                                             "border-radius:9px;\n"
                                             "color: rgb(243, 223, 162);\n"
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
                                             "color: rgb(3, 37, 108);\n"
                                             "background-color: #9FB1BC;\n"
                                             "}\n"
                                             "#botaoRegistrar:hover\n"
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
        self.tabelaFuncionario.horizontalHeader().setDefaultSectionSize(254)
        self.tabelaFuncionario.horizontalHeader().setStretchLastSection(False)
        self.tabelaFuncionario.verticalHeader().setVisible(False)
        self.tabelaFuncionario.verticalHeader().setDefaultSectionSize(65)
        self.verticalLayout.addWidget(self.tabelaFuncionario)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.botaoRegistrar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoRegistrar.setObjectName("botaoRegistrar")
        self.horizontalLayout.addWidget(self.botaoRegistrar)
        self.botaoRegistrar.clicked.connect(
            lambda: self.switchToRegistrar(telaGerenciarFuncionario)
        )
        self.botaoRemover = QtWidgets.QPushButton(self.centralwidget)
        self.botaoRemover.setObjectName("botaoRemover")
        self.horizontalLayout.addWidget(self.botaoRemover)
        self.botaoRemover.clicked.connect(self.remover)
        self.botaoAlterar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoAlterar.setObjectName("botaoAlterar")
        self.horizontalLayout.addWidget(self.botaoAlterar)
        self.botaoAlterar.clicked.connect(
            lambda: self.switchToAlterar(telaGerenciarFuncionario)
        )
        self.botaoSair = QtWidgets.QPushButton(self.centralwidget)
        self.botaoSair.setObjectName("botaoSair")
        self.botaoSair.clicked.connect(
            lambda: self.switchSair(telaGerenciarFuncionario)
        )
        self.horizontalLayout.addWidget(self.botaoSair)
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
        self.botaoRegistrar.setText(_translate(
            "telaGerenciarFuncionario", "Registrar"))
        self.botaoRemover.setText(_translate(
            "telaGerenciarFuncionario", "Remover"))
        self.botaoAlterar.setText(_translate(
            "telaGerenciarFuncionario", "Alterar"))
        self.botaoSair.setText(_translate(
            "telaGerenciarFuncionario", "Sair"))
        self.updateTable()
        self.tabelaFuncionario.setEditTriggers( QtWidgets.QTableWidget.NoEditTriggers)        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    telaGerenciarFuncionario = QtWidgets.QMainWindow()
    ui = Ui_telaGerenciarFuncionario()
    ui.setupUi(telaGerenciarFuncionario)
    telaGerenciarFuncionario.show()
    sys.exit(app.exec_())
