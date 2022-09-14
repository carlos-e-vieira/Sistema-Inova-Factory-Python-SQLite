import sys

from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow, QMessageBox

from View.tela_principal import Ui_Tela_Principal
from Controller.controller_usuarios import ControllerUsuarios

class ControllerPrincipal(QMainWindow, Ui_Tela_Principal):
    def __init__(self, usuario):
        super(ControllerPrincipal, self).__init__()
        self.setupUi(self)

        # ESCONTE BARRA DE TAREFAS
        self.setWindowFlag(Qt.FramelessWindowHint)
        # ICONE DO SISTEMA
        icone_inovafactory = QIcon('View/imagens/icone.png')
        self.setWindowIcon(icone_inovafactory)

        # OBJETOS
        self.tela_usuarios = ControllerUsuarios()
        # NÍVEL DE ACESSO DO USUÁRIO
        if usuario.lower() == 'usuário':
            self.btn_menu_usuarios.setEnabled(False)

        # -=-=-=-=-=-= BOTÕES MENUS -=-=-=-=-=-=-=-=-=-=-=-=
        # BTN HOME
        icone_btn_home = QIcon('View/imagens/btn-home.png')
        self.btn_menu_home.setIcon(icone_btn_home)
        self.btn_menu_home.setIconSize(QSize(33, 33))
        self.btn_menu_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.tela_home))

        # BTN CLIENTES
        icone_btn_clientes = QIcon('View/imagens/btn-clientes.png')
        self.btn_menu_clientes.setIcon(icone_btn_clientes)
        self.btn_menu_clientes.setIconSize(QSize(33, 33))

        # BTN SERVIÇOS
        icone_btn_servicos = QIcon('View/imagens/btn-servicos.png')
        self.btn_menu_servicos.setIcon(icone_btn_servicos)
        self.btn_menu_servicos.setIconSize(QSize(33, 33))

        # BTN RELATÓRIOS
        icone_btn_relatorios = QIcon('View/imagens/btn-relatorios.png')
        self.btn_menu_relatorios.setIcon(icone_btn_relatorios)
        self.btn_menu_relatorios.setIconSize(QSize(33, 33))

        # BTN FINANCEIRO
        icone_btn_financeiro = QIcon('View/imagens/btn-financeiro.png')
        self.btn_menu_financeiro.setIcon(icone_btn_financeiro)
        self.btn_menu_financeiro.setIconSize(QSize(33, 33))

        # BTN USUARIOS
        icone_btn_usuarios = QIcon('View/imagens/btn-usuarios.png')
        self.btn_menu_usuarios.setIcon(icone_btn_usuarios)
        self.btn_menu_usuarios.setIconSize(QSize(33, 33))
        self.btn_menu_usuarios.clicked.connect(self.abrir_tela_usuarios)

        # BTN SOBRE
        icone_btn_sobre = QIcon('View/imagens/btn-sobre.png')
        self.btn_menu_sobre.setIcon(icone_btn_sobre)
        self.btn_menu_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.tela_sobre))

        # BTN LOGOF
        icone_btn_logof = QIcon('View/imagens/btn-logof.png')
        self.btn_menu_logof.setIcon(icone_btn_logof)

        # BTN SAIR
        icone_btn_sair = QIcon('View/imagens/btn-sair.png')
        self.btn_menu_sair.setIcon(icone_btn_sair)
        self.btn_menu_sair.clicked.connect(self.fecha_sistema)




        # BOTÕES TELA USUÁRIOS
        self.btn_menu_usuarios.clicked.connect(lambda: self.Pages.setCurrentWidget(self.tela_usuarios))
        #self.btn_abre_form_usuarios.clicked.connect(self.abre_form_usuarios)

    # FECHAM O SISTEMA COM CAIXA DE DIALOGO
    def fecha_sistema(self, evento):
        msg = QMessageBox.question(self, "Mensagem", "Você deseja realmente sair do sistema?",
                                    QMessageBox.Yes | QMessageBox.Cancel)

        if msg == QMessageBox.Yes:
            sys.exit(1)
        else:
            pass

    def abrir_tela_usuarios(self):
        self.tela_usuarios.show()



