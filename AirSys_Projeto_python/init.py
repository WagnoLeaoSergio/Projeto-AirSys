import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from views.telaLogin.telaLogin import Ui_Login


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())