import sys

from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget, QMessageBox

from Model.dao import DAO
from View.tela_login import Ui_Tela_Login
from Controller.controller_principal import ControllerPrincipal
from Model.login_dao import LoginDAO

class ControllerLogin(QWidget, Ui_Tela_Login):
    def __init__(self) -> None:
        super(ControllerLogin, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle('Login do Sistema Inova Factory')

        # ICONE DO SISTEMA
        icone_sistema = QIcon('View/imagens/icone.png')
        self.setWindowIcon(icone_sistema)

        self.btn_login.clicked.connect(self.verifica_login)

    def verifica_login(self):
        self.usuario = LoginDAO()
        autenticado = self.usuario.verifica_usuario(self.input_login.text().upper(), self.input_senha.text())

        if autenticado.lower() == 'administrador' or autenticado.lower() == 'usuário':
            self.janela = ControllerPrincipal(autenticado.lower())
            self.janela.show()
            self.close()
        else:
            if self.tentativas < 3:
                self.exibir_popup_aviso('Erro ao acessar', f'Login ou senha inválidos '
                                                     f'\n\nTentativa: {self.tentativas +1} de 3')
                self.tentativas +=1

            if self.tentativas == 3:
                # bloquear usuário
                dao = DAO()
                dao.fecha_conexao()
                sys.exit(0)

    def exibir_popup_aviso(self, titulo, mensagen):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle(titulo)
        msg.setText(mensagen)
        msg.exec_()