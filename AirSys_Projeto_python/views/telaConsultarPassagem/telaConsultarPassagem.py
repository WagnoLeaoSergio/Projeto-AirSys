# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaConsultarPassagem.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append("../../")
import views.recursos.recursos_rc

class Ui_telaOpcoesCliente(object):
    def setupUi(self, telaOpcoesCliente):
        telaOpcoesCliente.setObjectName("telaOpcoesCliente")
        telaOpcoesCliente.resize(857, 508)
        telaOpcoesCliente.setStyleSheet("#telaOpcoesCliente\n"
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
                                        "#botaoComprar\n"
                                        "{\n"
                                        "font: 14pt \"Bitstream Vera Sans\";\n"
                                        "border-radius:9px;\n"
                                        "color: rgb(3, 37, 108);\n"
                                        "background-color: #9FB1BC;\n"
                                        "}\n"
                                        "#botaoComprar:hover\n"
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
        self.centralwidget = QtWidgets.QWidget(telaOpcoesCliente)
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
        self.tabelaCliente.setShowGrid(False)
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
        self.tabelaCliente.horizontalHeader().setDefaultSectionSize(167)
        self.tabelaCliente.horizontalHeader().setStretchLastSection(False)
        self.tabelaCliente.verticalHeader().setVisible(False)
        self.tabelaCliente.verticalHeader().setDefaultSectionSize(65)
        self.verticalLayout.addWidget(self.tabelaCliente)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.botaoComprar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoComprar.setObjectName("botaoComprar")
        self.horizontalLayout.addWidget(self.botaoComprar)
        self.botaoReservar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoReservar.setObjectName("botaoReservar")
        self.horizontalLayout.addWidget(self.botaoReservar)
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
        item = self.tabelaCliente.verticalHeaderItem(0)
        item.setText(_translate("telaOpcoesCliente", "New Row"))
        item = self.tabelaCliente.verticalHeaderItem(1)
        item.setText(_translate("telaOpcoesCliente", "New Row"))
        item = self.tabelaCliente.verticalHeaderItem(2)
        item.setText(_translate("telaOpcoesCliente", "New Row"))
        item = self.tabelaCliente.verticalHeaderItem(3)
        item.setText(_translate("telaOpcoesCliente", "New Row"))
        item = self.tabelaCliente.verticalHeaderItem(4)
        item.setText(_translate("telaOpcoesCliente", "New Row"))
        item = self.tabelaCliente.verticalHeaderItem(5)
        item.setText(_translate("telaOpcoesCliente", "New Row"))
        item = self.tabelaCliente.verticalHeaderItem(6)
        item.setText(_translate("telaOpcoesCliente", "New Row"))
        item = self.tabelaCliente.verticalHeaderItem(7)
        item.setText(_translate("telaOpcoesCliente", "New Row"))
        item = self.tabelaCliente.horizontalHeaderItem(0)
        item.setText(_translate("telaOpcoesCliente", "New Column"))
        item = self.tabelaCliente.horizontalHeaderItem(1)
        item.setText(_translate("telaOpcoesCliente", "codigo"))
        item = self.tabelaCliente.horizontalHeaderItem(2)
        item.setText(_translate("telaOpcoesCliente", "nome"))
        item = self.tabelaCliente.horizontalHeaderItem(3)
        item.setText(_translate("telaOpcoesCliente", "cpf"))
        item = self.tabelaCliente.horizontalHeaderItem(4)
        item.setText(_translate("telaOpcoesCliente", "numVendas"))
        self.botaoComprar.setText(_translate("telaOpcoesCliente", "Comprar"))
        self.botaoReservar.setText(_translate("telaOpcoesCliente", "Reservar"))
        self.botaoVoltar.setText(_translate("telaOpcoesCliente", "Sair"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    telaOpcoesCliente = QtWidgets.QMainWindow()
    ui = Ui_telaOpcoesCliente()
    ui.setupUi(telaOpcoesCliente)
    telaOpcoesCliente.show()
    sys.exit(app.exec_())
