# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaConsultarPassagem.ui'
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


class Ui_telaConsultarPassagem(object):
    def __init__(self):
        self.telaAnterior = ""

    def getTelaAnterior(self):
        return self.telaAnterior

    def setTelaAnterior(self, nomeTela):
        self.telaAnterior = nomeTela

    def updateTable(self):
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
        for row in range(self.numRows):
            for column in range(self.numColumns):
                self.tabelaPassagem.setItem(
                    row, column, QTableWidgetItem((data[row][column]))
                )

    def switchSair(self, ui):
        from views.telaOpcoesPassagem.telaOpcoesPassagem import Ui_telaOpcoesPassagem
        self.tela = QtWidgets.QMainWindow()
        self.opPassagem = Ui_telaOpcoesPassagem()
        self.opPassagem.setupUi(self.tela)
        self.opPassagem.setTelaAnterior(self.telaAnterior)
        ui.hide()
        self.tela.show()

    def switchToVender(self, ui):
        from views.telaVenderPassagem.telaVenderPassagem import Ui_telaVendaPassagem
        cod = self.tabelaPassagem.item(self.tabelaPassagem.currentRow(), 0).text()
        self.tela = QtWidgets.QMainWindow()
        self.pVender = Ui_telaVendaPassagem(self, cod)
        self.pVender.setupUi(self.tela)
        self.tela.show()

    def switchToReservar(self, ui):
        from views.telaReservarPassagem.telaReservarPassagem import Ui_telaReservaPassagem
        cod = self.tabelaPassagem.item(self.tabelaPassagem.currentRow(), 0).text()
        self.tela = QtWidgets.QMainWindow()
        self.pReservar = Ui_telaReservaPassagem(self, cod)
        self.pReservar.setupUi(self.tela)
        self.tela.show()

    def setupUi(self, telaConsultarPassagem):
        telaConsultarPassagem.setObjectName("telaConsultarPassagem")
        telaConsultarPassagem.resize(857, 508)
        telaConsultarPassagem.setStyleSheet("#telaConsultarPassagem\n"
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
                                            "#botaoVender\n"
                                            "{\n"
                                            "font: 14pt \"Bitstream Vera Sans\";\n"
                                            "border-radius:9px;\n"
                                            "color: rgb(3, 37, 108);\n"
                                            "background-color: #9FB1BC;\n"
                                            "}\n"
                                            "#botaoVender:hover\n"
                                            "{\n"
                                            "font: 14pt \"Bitstream Vera Sans\";\n"
                                            "border-radius:9px;\n"
                                            "background-color: #6E8898;\n"
                                            "}\n"
                                            "\n"
                                            "\n"
                                            "#botaoReservar\n"
                                            "{\n"
                                            "font: 14pt \"Bitstream Vera Sans\";\n"
                                            "border-radius:9px;\n"
                                            "color: rgb(3, 37, 108);\n"
                                            "background-color: #9FB1BC;\n"
                                            "}\n"
                                            "#botaoReservar:hover\n"
                                            "{\n"
                                            "font: 14pt \"Bitstream Vera Sans\";\n"
                                            "border-radius:9px;\n"
                                            "background-color: #6E8898;\n"
                                            "}")
        self.centralwidget = QtWidgets.QWidget(telaConsultarPassagem)
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
        self.tabelaPassagem.setShowGrid(False)
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
        self.tabelaPassagem.horizontalHeader().setDefaultSectionSize(240)
        self.tabelaPassagem.horizontalHeader().setStretchLastSection(False)
        self.tabelaPassagem.verticalHeader().setVisible(False)
        self.tabelaPassagem.verticalHeader().setDefaultSectionSize(65)
        self.verticalLayout.addWidget(self.tabelaPassagem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.botaoVender = QtWidgets.QPushButton(self.centralwidget)
        self.botaoVender.setObjectName("botaoVender")
        self.horizontalLayout.addWidget(self.botaoVender)
        self.botaoVender.clicked.connect(
            lambda: self.switchToVender(telaConsultarPassagem)
        )
        self.botaoReservar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoReservar.setObjectName("botaoReservar")
        self.horizontalLayout.addWidget(self.botaoReservar)
        self.botaoReservar.clicked.connect(
            lambda: self.switchToReservar(telaConsultarPassagem)
        )
        self.botaoSair = QtWidgets.QPushButton(self.centralwidget)
        self.botaoSair.setObjectName("botaoSair")
        self.horizontalLayout.addWidget(self.botaoSair)
        self.botaoSair.clicked.connect(
            lambda: self.switchSair(telaConsultarPassagem)
        )
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        telaConsultarPassagem.setCentralWidget(self.centralwidget)

        self.retranslateUi(telaConsultarPassagem)
        QtCore.QMetaObject.connectSlotsByName(telaConsultarPassagem)

    def retranslateUi(self, telaConsultarPassagem):
        _translate = QtCore.QCoreApplication.translate
        telaConsultarPassagem.setWindowTitle(
            _translate("telaConsultarPassagem", "AirSys - COnsultar Passagem"))
        item = self.tabelaPassagem.verticalHeaderItem(0)
        item.setText(_translate("telaConsultarPassagem", "New Row"))
        item = self.tabelaPassagem.verticalHeaderItem(1)
        item.setText(_translate("telaConsultarPassagem", "New Row"))
        item = self.tabelaPassagem.verticalHeaderItem(2)
        item.setText(_translate("telaConsultarPassagem", "New Row"))
        item = self.tabelaPassagem.verticalHeaderItem(3)
        item.setText(_translate("telaConsultarPassagem", "New Row"))
        item = self.tabelaPassagem.verticalHeaderItem(4)
        item.setText(_translate("telaConsultarPassagem", "New Row"))
        item = self.tabelaPassagem.verticalHeaderItem(5)
        item.setText(_translate("telaConsultarPassagem", "New Row"))
        item = self.tabelaPassagem.verticalHeaderItem(6)
        item.setText(_translate("telaConsultarPassagem", "New Row"))
        item = self.tabelaPassagem.verticalHeaderItem(7)
        item.setText(_translate("telaConsultarPassagem", "New Row"))
        item = self.tabelaPassagem.horizontalHeaderItem(0)
        item.setText(_translate("telaConsultarPassagem", "New Column"))
        item = self.tabelaPassagem.horizontalHeaderItem(1)
        item.setText(_translate("telaConsultarPassagem", "codigo"))
        item = self.tabelaPassagem.horizontalHeaderItem(2)
        item.setText(_translate("telaConsultarPassagem", "nome"))
        item = self.tabelaPassagem.horizontalHeaderItem(3)
        item.setText(_translate("telaConsultarPassagem", "cpf"))
        item = self.tabelaPassagem.horizontalHeaderItem(4)
        item.setText(_translate("telaConsultarPassagem", "numVendas"))
        self.botaoVender.setText(_translate(
            "telaConsultarPassagem", "Vender"))
        self.botaoReservar.setText(_translate(
            "telaConsultarPassagem", "Reservar"))
        self.botaoSair.setText(_translate("telaConsultarPassagem", "Sair"))
        self.updateTable()
        self.tabelaPassagem.setEditTriggers( QtWidgets.QTableWidget.NoEditTriggers)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    telaConsultarPassagem = QtWidgets.QMainWindow()
    ui = Ui_telaConsultarPassagem()
    ui.setupUi(telaConsultarPassagem)
    telaConsultarPassagem.show()
    sys.exit(app.exec_())
