# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaInserirPassagem.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append("../../")
import views.recursos.recursos_rc

class Ui_telaInserirPassagem(object):
    def setupUi(self, telaInserirPassagem):
        telaInserirPassagem.setObjectName("telaInserirPassagem")
        telaInserirPassagem.resize(407, 538)
        telaInserirPassagem.setMinimumSize(QtCore.QSize(407, 538))
        telaInserirPassagem.setMaximumSize(QtCore.QSize(407, 538))
        telaInserirPassagem.setStyleSheet("#telaInserirPassagem\n"
                                          "{\n"
                                          "background-image: url(:/fundos/fundo3.jpg);\n"
                                          "}\n"
                                          "#frameDados\n"
                                          "{\n"
                                          "background-color: rgba(13, 125, 159, 80);\n"
                                          "}\n"
                                          "#labelInfo\n"
                                          "{\n"
                                          "font: 13pt \"Noto Serif Malayalam\";\n"
                                          "color: rgb(243, 234, 225);\n"
                                          "}\n"
                                          "\n"
                                          "#campoCodigo\n"
                                          "{\n"
                                          "color: rgb(243, 234, 225);\n"
                                          "background-color: rgba(37, 128, 197, 150);\n"
                                          "}\n"
                                          "\n"
                                          "#campoOrigem\n"
                                          "{\n"
                                          "color: rgb(243, 234, 225);\n"
                                          "background-color: rgba(37, 128, 197, 150);\n"
                                          "}\n"
                                          "\n"
                                          "#campoDestino\n"
                                          "{\n"
                                          "color: rgb(243, 234, 225);\n"
                                          "background-color: rgba(37, 128, 197, 150);\n"
                                          "}\n"
                                          "\n"
                                          "#campoData\n"
                                          "{\n"
                                          "color: rgb(243, 234, 225);\n"
                                          "background-color: rgba(37, 128, 197, 150);\n"
                                          "}\n"
                                          "\n"
                                          "#campoCompanhia\n"
                                          "{\n"
                                          "color: rgb(243, 234, 225);\n"
                                          "background-color: rgba(37, 128, 197, 150);\n"
                                          "}\n"
                                          "\n"
                                          "#campoAssento\n"
                                          "{\n"
                                          "color: rgb(243, 234, 225);\n"
                                          "background-color: rgba(37, 128, 197, 150);\n"
                                          "}\n"
                                          "\n"
                                          "#campoPreco\n"
                                          "{\n"
                                          "color: rgb(243, 234, 225);\n"
                                          "background-color: rgba(37, 128, 197, 150);\n"
                                          "}\n"
                                          "\n"
                                          "#botaoSubmeter\n"
                                          "{\n"
                                          "color: rgb(8, 76, 97);\n"
                                          "font: 12pt \"Noto Serif Malayalam\";\n"
                                          "border-radius:5px;\n"
                                          "background-color: rgb(238, 219, 159);\n"
                                          "}\n"
                                          "#botaoSubmeter:hover\n"
                                          "{\n"
                                          "color: rgb(8, 76, 97);\n"
                                          "font: 12pt \"Noto Serif Malayalam\";\n"
                                          "border-radius:5px;\n"
                                          "background-color: rgb(194, 178, 129);\n"
                                          "}")
        self.centralwidget = QtWidgets.QWidget(telaInserirPassagem)
        self.centralwidget.setObjectName("centralwidget")
        self.frameDados = QtWidgets.QFrame(self.centralwidget)
        self.frameDados.setGeometry(QtCore.QRect(40, 30, 331, 461))
        self.frameDados.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameDados.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameDados.setObjectName("frameDados")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frameDados)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 60, 231, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.campoCodigo = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.campoCodigo.setObjectName("campoCodigo")
        self.verticalLayout.addWidget(self.campoCodigo)
        self.campoOrigem = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.campoOrigem.setObjectName("campoOrigem")
        self.verticalLayout.addWidget(self.campoOrigem)
        self.campoDestino = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.campoDestino.setObjectName("campoDestino")
        self.verticalLayout.addWidget(self.campoDestino)
        self.campoData = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.campoData.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.campoData.setObjectName("campoData")
        self.verticalLayout.addWidget(self.campoData)
        self.campoCompanhia = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.campoCompanhia.setObjectName("campoCompanhia")
        self.verticalLayout.addWidget(self.campoCompanhia)
        self.campoAssento = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.campoAssento.setObjectName("campoAssento")
        self.verticalLayout.addWidget(self.campoAssento)
        self.campoPreco = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.campoPreco.setText("")
        self.campoPreco.setObjectName("campoPreco")
        self.verticalLayout.addWidget(self.campoPreco)
        self.labelInfo = QtWidgets.QLabel(self.frameDados)
        self.labelInfo.setGeometry(QtCore.QRect(0, 20, 331, 31))
        self.labelInfo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInfo.setObjectName("labelInfo")
        self.botaoSubmeter = QtWidgets.QPushButton(self.centralwidget)
        self.botaoSubmeter.setGeometry(QtCore.QRect(140, 500, 121, 31))
        self.botaoSubmeter.setObjectName("botaoSubmeter")
        telaInserirPassagem.setCentralWidget(self.centralwidget)

        self.retranslateUi(telaInserirPassagem)
        QtCore.QMetaObject.connectSlotsByName(telaInserirPassagem)

    def retranslateUi(self, telaInserirPassagem):
        _translate = QtCore.QCoreApplication.translate
        telaInserirPassagem.setWindowTitle(
            _translate("telaInserirPassagem", "MainWindow"))
        self.campoCodigo.setPlaceholderText(
            _translate("telaInserirPassagem", "CODIGO"))
        self.campoOrigem.setPlaceholderText(
            _translate("telaInserirPassagem", "ORIGEM"))
        self.campoDestino.setPlaceholderText(
            _translate("telaInserirPassagem", "DESTINO"))
        self.campoData.setPlaceholderText(
            _translate("telaInserirPassagem", "DATA"))
        self.campoCompanhia.setPlaceholderText(
            _translate("telaInserirPassagem", "COMPANHIA AÉREA"))
        self.campoAssento.setPlaceholderText(
            _translate("telaInserirPassagem", "ASSENTO"))
        self.campoPreco.setPlaceholderText(
            _translate("telaInserirPassagem", "PREÇO"))
        self.labelInfo.setText(_translate(
            "telaInserirPassagem", "Insira aqui os dados da passagem"))
        self.botaoSubmeter.setText(_translate(
            "telaInserirPassagem", "Submeter"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    telaInserirPassagem = QtWidgets.QMainWindow()
    ui = Ui_telaInserirPassagem()
    ui.setupUi(telaInserirPassagem)
    telaInserirPassagem.show()
    sys.exit(app.exec_())
