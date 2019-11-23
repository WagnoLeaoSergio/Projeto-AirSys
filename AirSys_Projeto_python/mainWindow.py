import sys
from PyQt5 import QtCore, QtWidgets

from views.telaLogin.telaLogin import Ui_Login

class MainWindow:
    """Main application window, handles the workflow of secondary windows"""
    def __init__(self):
        self.window = QtWidgets.QMainWindow()

    def show_login(self):
        ui = Ui_Login()
        ui.setupUi(self.window)
        self.window.show()

    def show_opcoes_funcionario(self):
        self.window = Ui_telaOpcoesFuncionario()
        self.window.switch_window.connect(self.show_window_two)
        self.login.close()
        self.window.show()
"""
    def show_window_two(self, text):
        self.window_two = WindowTwo(text)
        self.window.close()
        self.window_two.show()
"""