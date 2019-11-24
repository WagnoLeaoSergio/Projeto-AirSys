# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaGerenciarCliente.ui'
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

class Ui_telaGerenciarCliente:
    def __init__(self):
        self.telaAnterior = ""
        self.cList = controles.ListaClientes()

    def getTelaAnterior(self):
        return self.telaAnterior

    def setTelaAnterior(self, nomeTela):
        self.telaAnterior = nomeTela

    def updateTable(self):
        self.cData = self.cList.listarClientes()
        self.numRows = len(self.cData)
        self.numColumns = 6
        self.tabelaCliente.setRowCount(self.numRows)
        self.tabelaCliente.setColumnCount(self.numColumns)
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
                         passData["banco"],
                         ))
            j = j + 1
        for row in range(self.numRows):
            for column in range(self.numColumns):
                self.tabelaCliente.setItem(
                    row, column, QTableWidgetItem((data[row][column]))
                )
    def remover(self):
        # encotrar indice da linha selecionada:
        # indexes = self.tabelaCliente.selectionModel().selectedRows()
        # remvIndex = indexes[0].row()
        cod = self.tabelaCliente.item(self.tabelaCliente.currentRow(), 0).text()
        self.cList.removerCliente(cod)
        self.updateTable()


    def switchToRegistrar(self, ui):
        from views.telaInserirCliente.telaInserirCliente import Ui_telaInserirCliente
        self.tela = QtWidgets.QMainWindow()
        self.registrar = Ui_telaInserirCliente(self)
        self.registrar.setupUi(self.tela)
        self.tela.show()
        self.updateTable()

    def switchToAlterar(self, ui):
        from views.telaAlterarCliente.telaAlterarCliente import Ui_telaAlterarCliente
        cod = self.tabelaCliente.item(self.tabelaCliente.currentRow(), 0).text()
        self.tela = QtWidgets.QMainWindow()
        self.alterar = Ui_telaAlterarCliente(self, cod)
        self.alterar.setupUi(self.tela)
        self.tela.show()
        self.updateTable()

    def switchSair(self, ui):
        if self.telaAnterior == "Funcionario":
            from views.telaMenuFuncionario.telaOpcoesFuncionario import Ui_telaOpcoesFuncionario
            tela = QtWidgets.QMainWindow()
            menuFuncionario = Ui_telaOpcoesFuncionario()
            menuFuncionario.setupUi(tela)
            ui.hide()
            tela.show()
        elif self.telaAnterior == "Gerente":
            from views.telaMenuGerente.telaMenuGerente import Ui_telaOpcoesGerente                
            tela = QtWidgets.QMainWindow()
            menuGerente = Ui_telaOpcoesGerente()
            menuGerente.setupUi(tela)
            ui.hide()
            tela.show()

    def setupUi(self, telaGerenciarCliente):
        telaGerenciarCliente.setObjectName("telaGerenciarCliente")
        telaGerenciarCliente.resize(829, 567)
        telaGerenciarCliente.setStyleSheet("#telaGerenciarCliente\n"
                                           "{\n"
                                           "background-image: url(:/fundos/fundo3.jpg);\n"
                                           "}\n"
                                           "\n"
                                           "#tabelaCliente\n"
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
        self.centralwidget = QtWidgets.QWidget(telaGerenciarCliente)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabelaCliente = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabelaCliente.setFont(font)
        self.tabelaCliente.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.tabelaCliente.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tabelaCliente.setAutoScroll(True)
        self.tabelaCliente.setProperty("showDropIndicator", False)
        self.tabelaCliente.setAlternatingRowColors(False)
        self.tabelaCliente.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.tabelaCliente.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tabelaCliente.setShowGrid(True)
        self.tabelaCliente.setGridStyle(QtCore.Qt.SolidLine)
        self.tabelaCliente.setCornerButtonEnabled(False)
        self.tabelaCliente.setRowCount(13)
        self.tabelaCliente.setObjectName("tabelaCliente")
        self.tabelaCliente.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaCliente.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaCliente.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaCliente.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaCliente.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaCliente.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaCliente.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaCliente.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaCliente.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaCliente.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaCliente.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaCliente.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaCliente.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaCliente.setHorizontalHeaderItem(4, item)
        self.tabelaCliente.horizontalHeader().setVisible(False)
        self.tabelaCliente.horizontalHeader().setDefaultSectionSize(264)
        self.tabelaCliente.horizontalHeader().setStretchLastSection(False)
        self.tabelaCliente.verticalHeader().setVisible(False)
        self.tabelaCliente.verticalHeader().setDefaultSectionSize(65)
        self.verticalLayout.addWidget(self.tabelaCliente)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.botaoRegistrar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoRegistrar.setObjectName("botaoRegistrar")
        self.botaoRegistrar.clicked.connect(
            lambda: self.switchToRegistrar(telaGerenciarCliente)
        )
        self.horizontalLayout.addWidget(self.botaoRegistrar)
        self.botaoRemover = QtWidgets.QPushButton(self.centralwidget)
        self.botaoRemover.setObjectName("botaoRemover")
        self.horizontalLayout.addWidget(self.botaoRemover)
        self.botaoRemover.clicked.connect(self.remover)
        self.botaoAlterar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoAlterar.setObjectName("botaoAlterar")
        self.horizontalLayout.addWidget(self.botaoAlterar)
        self.botaoAlterar.clicked.connect(
            lambda: self.switchToAlterar(telaGerenciarCliente)
        )
        self.botaoSair = QtWidgets.QPushButton(self.centralwidget)
        self.botaoSair.setObjectName("botaoSair")
        self.botaoSair.clicked.connect(
            lambda: self.switchSair(telaGerenciarCliente)
        )
        self.horizontalLayout.addWidget(self.botaoSair)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        telaGerenciarCliente.setCentralWidget(self.centralwidget)

        self.retranslateUi(telaGerenciarCliente)
        QtCore.QMetaObject.connectSlotsByName(telaGerenciarCliente)

    def retranslateUi(self, telaGerenciarCliente):
        _translate = QtCore.QCoreApplication.translate
        telaGerenciarCliente.setWindowTitle(
            _translate("telaGerenciarCliente", "AirSys - Menu"))
        item = self.tabelaCliente.verticalHeaderItem(0)
        item.setText(_translate("telaGerenciarCliente", "New Row"))
        item = self.tabelaCliente.verticalHeaderItem(1)
        item.setText(_translate("telaGerenciarCliente", "New Row"))
        item = self.tabelaCliente.verticalHeaderItem(2)
        item.setText(_translate("telaGerenciarCliente", "New Row"))
        item = self.tabelaCliente.verticalHeaderItem(3)
        item.setText(_translate("telaGerenciarCliente", "New Row"))
        item = self.tabelaCliente.verticalHeaderItem(4)
        item.setText(_translate("telaGerenciarCliente", "New Row"))
        item = self.tabelaCliente.verticalHeaderItem(5)
        item.setText(_translate("telaGerenciarCliente", "New Row"))
        item = self.tabelaCliente.verticalHeaderItem(6)
        item.setText(_translate("telaGerenciarCliente", "New Row"))
        item = self.tabelaCliente.verticalHeaderItem(7)
        item.setText(_translate("telaGerenciarCliente", "New Row"))
        item = self.tabelaCliente.horizontalHeaderItem(0)
        item.setText(_translate("telaGerenciarCliente", "New Column"))
        item = self.tabelaCliente.horizontalHeaderItem(1)
        item.setText(_translate("telaGerenciarCliente", "codigo"))
        item = self.tabelaCliente.horizontalHeaderItem(2)
        item.setText(_translate("telaGerenciarCliente", "nome"))
        item = self.tabelaCliente.horizontalHeaderItem(3)
        item.setText(_translate("telaGerenciarCliente", "cpf"))
        item = self.tabelaCliente.horizontalHeaderItem(4)
        item.setText(_translate("telaGerenciarCliente", "numVendas"))
        self.botaoRegistrar.setText(_translate(
            "telaGerenciarCliente", "Registrar"))
        self.botaoRemover.setText(_translate(
            "telaGerenciarCliente", "Remover"))
        self.botaoAlterar.setText(_translate(
            "telaGerenciarCliente", "Alterar"))
        self.botaoSair.setText(_translate("telaGerenciarCliente", "Sair"))
        self.updateTable()
        self.tabelaCliente.setEditTriggers( QtWidgets.QTableWidget.NoEditTriggers)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    telaGerenciarCliente = QtWidgets.QMainWindow()
    ui = Ui_telaGerenciarCliente()
    ui.setupUi(telaGerenciarCliente)
    telaGerenciarCliente.show()
    sys.exit(app.exec_())
