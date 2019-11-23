# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaGerenciarPassagem.ui'
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


class Ui_telaOpcoesCliente(object):
    def setupUi(self, telaOpcoesCliente):
        telaOpcoesCliente.setObjectName("telaOpcoesCliente")
        telaOpcoesCliente.resize(829, 567)
        telaOpcoesCliente.setStyleSheet("#telaOpcoesCliente\n"
                                        "{\n"
                                        "background-image: url(:/fundos/fundo3.jpg);\n"
                                        "}\n"
                                        "\n"
                                        "#tabelaPassagem\n"
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
        self.centralwidget = QtWidgets.QWidget(telaOpcoesCliente)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabelaPassagem = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabelaPassagem.setFont(font)
        self.tabelaPassagem.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.tabelaPassagem.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tabelaPassagem.setAutoScroll(True)
        self.tabelaPassagem.setProperty("showDropIndicator", False)
        self.tabelaPassagem.setAlternatingRowColors(False)
        self.tabelaPassagem.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.tabelaPassagem.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tabelaPassagem.setShowGrid(True)
        self.tabelaPassagem.setGridStyle(QtCore.Qt.SolidLine)
        self.tabelaPassagem.setCornerButtonEnabled(False)
        self.tabelaPassagem.setRowCount(13)
        self.tabelaPassagem.setObjectName("tabelaPassagem")
        self.tabelaPassagem.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaPassagem.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaPassagem.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaPassagem.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaPassagem.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaPassagem.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaPassagem.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaPassagem.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaPassagem.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaPassagem.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaPassagem.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaPassagem.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaPassagem.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaPassagem.setHorizontalHeaderItem(4, item)
        self.tabelaPassagem.horizontalHeader().setVisible(False)
        self.tabelaPassagem.horizontalHeader().setDefaultSectionSize(195)
        self.tabelaPassagem.horizontalHeader().setStretchLastSection(False)
        self.tabelaPassagem.verticalHeader().setVisible(False)
        self.tabelaPassagem.verticalHeader().setDefaultSectionSize(65)
        self.verticalLayout.addWidget(self.tabelaPassagem)
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
        telaOpcoesCliente.setCentralWidget(self.centralwidget)

        self.retranslateUi(telaOpcoesCliente)
        QtCore.QMetaObject.connectSlotsByName(telaOpcoesCliente)

    def retranslateUi(self, telaOpcoesCliente):
        _translate = QtCore.QCoreApplication.translate
        telaOpcoesCliente.setWindowTitle(
            _translate("telaOpcoesCliente", "AirSys - Menu"))
        item = self.tabelaPassagem.verticalHeaderItem(0)
        item.setText(_translate("telaOpcoesCliente", "New Row"))
        item = self.tabelaPassagem.verticalHeaderItem(1)
        item.setText(_translate("telaOpcoesCliente", "New Row"))
        item = self.tabelaPassagem.verticalHeaderItem(2)
        item.setText(_translate("telaOpcoesCliente", "New Row"))
        item = self.tabelaPassagem.verticalHeaderItem(3)
        item.setText(_translate("telaOpcoesCliente", "New Row"))
        item = self.tabelaPassagem.verticalHeaderItem(4)
        item.setText(_translate("telaOpcoesCliente", "New Row"))
        item = self.tabelaPassagem.verticalHeaderItem(5)
        item.setText(_translate("telaOpcoesCliente", "New Row"))
        item = self.tabelaPassagem.verticalHeaderItem(6)
        item.setText(_translate("telaOpcoesCliente", "New Row"))
        item = self.tabelaPassagem.verticalHeaderItem(7)
        item.setText(_translate("telaOpcoesCliente", "New Row"))
        item = self.tabelaPassagem.horizontalHeaderItem(0)
        item.setText(_translate("telaOpcoesCliente", "New Column"))
        item = self.tabelaPassagem.horizontalHeaderItem(1)
        item.setText(_translate("telaOpcoesCliente", "codigo"))
        item = self.tabelaPassagem.horizontalHeaderItem(2)
        item.setText(_translate("telaOpcoesCliente", "nome"))
        item = self.tabelaPassagem.horizontalHeaderItem(3)
        item.setText(_translate("telaOpcoesCliente", "cpf"))
        item = self.tabelaPassagem.horizontalHeaderItem(4)
        item.setText(_translate("telaOpcoesCliente", "numVendas"))
        self.botaoInserir.setText(_translate("telaOpcoesCliente", "Inserir"))
        self.botaoRemover.setText(_translate("telaOpcoesCliente", "Remover"))
        self.botaoAlterar.setText(_translate("telaOpcoesCliente", "Alterar"))
        self.botaoVoltar.setText(_translate("telaOpcoesCliente", "Sair"))
        self.pList = controles.ListaPassagens()
        self.pData = self.pList.listarPassagens()
        self.numRows = len(self.pData)
        self.numColumns = 8
        self.tabelaPassagem.setRowCount(self.numRows)
        self.tabelaPassagem.setColumnCount(self.numColumns)
        j = 0
        data = []
        for i in self.pData:
            passData = i["element{0}".format(j)]
            del passData["_id"]
            data.append((passData["codigo"],
                         passData["origem"],
                         passData["destino"],
                         passData["data"],
                         passData["companhia"],
                         passData["assento"],
                         passData["preco"],
                         passData["dataCompra"]
                         ))
            j = j + 1
        print(self.pData)
        for row in range(self.numRows):
            for column in range(self.numColumns):
                self.tabelaPassagem.setItem(
                    row, column, QTableWidgetItem((data[row][column]))
                )
        self.tabelaPassagem.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    telaOpcoesCliente = QtWidgets.QMainWindow()
    ui = Ui_telaOpcoesCliente()
    ui.setupUi(telaOpcoesCliente)
    telaOpcoesCliente.show()
    sys.exit(app.exec_())
