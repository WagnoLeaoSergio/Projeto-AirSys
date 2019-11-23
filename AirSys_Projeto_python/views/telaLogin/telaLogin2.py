# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaLogin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
import recursos_rc
from PyQt5 import QtCore, QtGui, QtWidgets

sys.path.append("../../")

import controles


class Login(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def checarCredenciais(self):
        cod = self.CampoCodigo.text()
        senha = self.CampoSenha.text()

        if cod == "" or senha == "":
            print("Digite codigo e senha validos")
        else:
            fList = controles.ListaFuncionarios()
            gList = controles.ListaGerentes()

            buscaF = fList.buscarFuncionario(codigo=cod)
            buscaG = gList.buscarGerente(codigo=cod)

            if buscaF is not None:
                print("Pode logar funcionario!")
                self.switch_window.emit()
            elif buscaG is not None:
                print("Pode logar gerente!")
                sys.path.append("../")
                from telaMenuGerente.telaMenuGerente import Ui_telaOpcoesGerente
                self.hide()
                self.telaOpcoes = QtWidgets.QMainWindow()
                self.opcoesGerente = Ui_telaOpcoesGerente()
                self.opcoesGerente.setupUi(self.telaOpcoes)
                self.telaOpcoes.show()
            else:
                print("Usuario ou senha incorretos")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(425, 504)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(169)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(425, 504))
        MainWindow.setMaximumSize(QtCore.QSize(425, 504))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("#MainWindow\n"
                                 "{\n"
                                 "background-image: url(:/newPrefix/fundo.jpg);\n"
                                 "}\n"
                                 "\n"
                                 "#frame\n"
                                 "{\n"
                                 "background-color: rgba(46, 82, 102, 200);\n"
                                 "}\n"
                                 "\n"
                                 "#label_codigo\n"
                                 "{\n"
                                 "color: rgb(246, 238, 226);\n"
                                 "font: 75 14pt \"MathJax_SansSerif\";\n"
                                 "}\n"
                                 "\n"
                                 "#CampoCodigo\n"
                                 "{\n"
                                 "color: rgb(211, 208, 203);\n"
                                 "background-color: #6E8898;\n"
                                 "}\n"
                                 "\n"
                                 "#label_senha\n"
                                 "{\n"
                                 "color: rgb(246, 238, 226);\n"
                                 "font: 75 14pt \"MathJax_SansSerif\";\n"
                                 "}\n"
                                 "\n"
                                 "#CampoSenha\n"
                                 "{\n"
                                 "color: rgb(211, 208, 203);\n"
                                 "background-color: #6E8898;\n"
                                 "}\n"
                                 "\n"
                                 "#label\n"
                                 "{\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "font: 75 15pt \"Noto Serif Khmer\";\n"
                                 "}\n"
                                 "\n"
                                 "#BotaoLogar\n"
                                 "{\n"
                                 "color:#D3D0CB;\n"
                                 "background-color: rgb(66, 85, 99);\n"
                                 "border-radius:10px;\n"
                                 "}\n"
                                 "#BotaoLogar:hover\n"
                                 "{\n"
                                 "background-color: rgb(122, 168, 199);\n"
                                 "border-radius:10px;\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(15, 30, 391, 451))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK TC Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.CampoCodigo = QtWidgets.QLineEdit(self.frame)
        self.CampoCodigo.setGeometry(QtCore.QRect(30, 220, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CampoCodigo.setFont(font)
        self.CampoCodigo.setAutoFillBackground(False)
        self.CampoCodigo.setStyleSheet("")
        self.CampoCodigo.setText("")
        self.CampoCodigo.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.CampoCodigo.setPlaceholderText("")
        self.CampoCodigo.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.CampoCodigo.setObjectName("CampoCodigo")
        self.CampoSenha = QtWidgets.QLineEdit(self.frame)
        self.CampoSenha.setGeometry(QtCore.QRect(30, 280, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CampoSenha.setFont(font)
        self.CampoSenha.setStyleSheet("")
        self.CampoSenha.setText("")
        self.CampoSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.CampoSenha.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.CampoSenha.setPlaceholderText("")
        self.CampoSenha.setObjectName("CampoSenha")
        self.BotaoLogar = QtWidgets.QPushButton(self.frame)
        # BOTAO
        self.BotaoLogar.clicked.connect(self.checarCredenciais)
        self.BotaoLogar.setGeometry(QtCore.QRect(140, 370, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK TC")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.BotaoLogar.setFont(font)
        self.BotaoLogar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.BotaoLogar.setStyleSheet("")
        self.BotaoLogar.setObjectName("BotaoLogar")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 100, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Khmer")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_codigo = QtWidgets.QLabel(self.frame)
        self.label_codigo.setGeometry(QtCore.QRect(30, 190, 101, 31))
        self.label_codigo.setObjectName("label_codigo")
        self.label_senha = QtWidgets.QLabel(self.frame)
        self.label_senha.setGeometry(QtCore.QRect(30, 250, 101, 31))
        self.label_senha.setObjectName("label_senha")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AirSys - Login"))
        self.BotaoLogar.setText(_translate("MainWindow", "Logar"))
        self.BotaoLogar.setShortcut(_translate("MainWindow", "Return"))
        self.label.setText(_translate(
            "MainWindow", "Entre com seu código e senha"))
        self.label_codigo.setText(_translate("MainWindow", "Codigo"))
        self.label_senha.setText(_translate("MainWindow", "Senha"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
