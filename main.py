from PySide2.QtWidgets import (QApplication)
from Controller.controller_login import ControllerLogin
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tela_login = ControllerLogin()
    tela_login.show()
    app.exec_()
