from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from View.tela_usuarios import Ui_Tela_Usuarios
from Model.usuarios_dao import UsuariosDAO

class ControllerUsuarios(QWidget, Ui_Tela_Usuarios):
    def __init__(self) -> None:
        super(ControllerUsuarios, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Cadastrar Novo Usuário')
        icone_inovafactory = QIcon('View/imagens/icone.png')
        self.setWindowIcon(icone_inovafactory)

        # TABELA USUÁRIOS - SELECIONA A LINHA INTEIRA
        self.tb_lista_usuarios.setSelectionBehavior(self.tb_lista_usuarios.SelectRows)

        # LISTA USUÁRIOS NA TABELA
        self.listar_todos_usuarios()

        # ABRE FORM CADASTRAR USUÁRIO
        self.btn_form_cadastrar_usuario.clicked.connect(lambda: self.Pages.setCurrentWidget(self.tela_form_cadastrar_usuario))
        # BTN CADASTRAR USUÁRIO
        self.btn_salvar_cadastro_usuario.clicked.connect(self.cadastrar_usuario)
        # BTN CANCELAR CADASTRO
        self.btn_cancelar_cadastro_usuario.clicked.connect(self.cancelar_cadastro)

        # EXCLUIR USUARIO ATRAVÉS DA TABELA
        self.btn_excluir_usuario.clicked.connect(self.excluir_usuario)

        # ABRE FORM ALTERAR USUÁRIO
        self.btn_form_alterar_usuario.clicked.connect(self.listar_usuario_form_alterar)
        # BTN CANCELAR ALTERAÇÃO USUÁRIO
        self.btn_cancelar_alterar_usuario.clicked.connect(lambda: self.Pages.setCurrentWidget(self.tela_principal_usuarios))
        # BTN ALTERAR USUÁRIO
        self.btn_salvar_alterar_usuario.clicked.connect(self.atualizar_usuario)

        # BTN PESQUISAR USUÁRIO
        self.btn_pesquisar_usuario.clicked.connect(self.pesquisar_usuario)
        # BTN LIMPAR FILTRO DE PESQUISA
        self.btn_limpa_pesquisar_usuario.clicked.connect(self.limpar_filtro_pesquisar)

    def limpa_inputs_form_cadastro(self):
        self.input_cadastrar_nome_usuario.setText('')
        self.input_cadastrar_login_usuario.setText('')
        self.input_cadastrar_senha_usuario.setText('')
        self.input_cadastrar_senha_2_usuario.setText('')

    def cancelar_cadastro(self):
        self.limpa_inputs_form_cadastro()
        self.Pages.setCurrentWidget(self.tela_principal_usuarios)

    def cadastrar_usuario(self):
        nome = self.input_cadastrar_nome_usuario.text()
        login = self.input_cadastrar_login_usuario.text()
        senha = self.input_cadastrar_senha_usuario.text()
        acesso = self.cb_cadastrar_acesso_usuario.currentText()

        if nome != '' and login != '' and senha != '' and acesso != '':
            if self.input_cadastrar_senha_usuario.text() != self.input_cadastrar_senha_2_usuario.text():
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle('Senhas Divergentes')
                msg.setText('As senhas não são iguais.')
                msg.exec_()
                return None

            usuariosDAO = UsuariosDAO()
            usuariosDAO.cadastrar_usuario(nome, login, senha, acesso)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Confirmação de Cadastro')
            msg.setText(f'Cadastro do usuário *{nome.upper()}* realizado com sucesso!')
            msg.exec_()

            # LIMPA INPUTS
            self.limpa_inputs_form_cadastro()

            # ATUALIZA TABELA
            self.listar_todos_usuarios()

            # FECHA JANELA AUTOMATICAMENTE
            self.Pages.setCurrentWidget(self.tela_principal_usuarios)

        else:
            msg_e = QMessageBox()
            msg_e.setIcon(QMessageBox.Warning)
            msg_e.setWindowTitle('ERRO')
            msg_e.setText('Preencha todos os campos')
            msg_e.exec_()
            return None

    def listar_todos_usuarios(self):
        usuarioDAO = UsuariosDAO()
        todos_usuarios = usuarioDAO.listar_todos_usuarios()

        self.tb_lista_usuarios.clearContents()
        self.tb_lista_usuarios.setRowCount(len(todos_usuarios))

        for linha, texto in enumerate(todos_usuarios):
            for coluna, dado in enumerate(texto):
                self.tb_lista_usuarios.setItem(linha, coluna, QTableWidgetItem(str(dado)))

    def excluir_usuario(self):
        usuarioDAO = UsuariosDAO()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle('Excluir Usuário')
        msg.setInformativeText('Você deseja realmente excluir o usuário do sistema?')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resposta = msg.exec()

        if resposta == QMessageBox.Yes:
            id = self.tb_lista_usuarios.selectionModel().currentIndex().siblingAtColumn(0).data()
            resultado = usuarioDAO.excluir_usuario(id)
            self.listar_todos_usuarios()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('usuários')
            msg.setText(resultado)
            msg.exec()

    def atualizar_usuario(self):
        id = self.input_alterar_id_usuario.text()
        nome = self.input_alterar_nome_usuario.text()
        login = self.input_alterar_login_usuario.text()
        senha = self.input_alterar_senha_usuario.text()
        acesso = self.cb_alterar_acesso_usuario.currentText()

        if nome != '' and login != '' and senha != '' and acesso != '':
            if self.input_alterar_senha_usuario.text() != self.input_alterar_senha_2_usuario.text():
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle('Senhas Divergentes')
                msg.setText('As senhas não são iguais.')
                msg.exec_()
                return None

            usuariosDAO = UsuariosDAO()
            usuariosDAO.atualizar_usuario(id, nome, login, senha, acesso)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Confirmação de Alteração')
            msg.setText(f'Altaração do usuário *{nome.upper()}* realizada com sucesso!')
            msg.exec_()

            # ATUALIZA TABELA
            self.listar_todos_usuarios()

            # FECHA JANELA AUTOMATICAMENTE
            self.Pages.setCurrentWidget(self.tela_principal_usuarios)
        else:
            msg_e = QMessageBox()
            msg_e.setIcon(QMessageBox.Warning)
            msg_e.setWindowTitle('ERRO')
            msg_e.setText('Preencha todos os campos')
            msg_e.exec_()
            return None

    def listar_usuario_form_alterar(self):
        try:
            id: QTableWidgetItem = self.tb_lista_usuarios.selectedItems()[0]
        except IndexError:
            return

        id_selecionado = id.text()

        usuarioDAO = UsuariosDAO
        self.usuario_pesquisado = usuarioDAO.listar_usuario(self, id_selecionado)

        # ABRE O FORM COM OS INPUTS PREENCHIDOS
        self.Pages.setCurrentWidget(self.tela_form_alterar_usuario)

        self.input_alterar_id_usuario.setText(id_selecionado)
        self.input_alterar_nome_usuario.setText(self.usuario_pesquisado[0][1])
        self.input_alterar_login_usuario.setText(self.usuario_pesquisado[0][2])
        self.input_alterar_senha_usuario.setText(self.usuario_pesquisado[0][3])
        self.input_alterar_senha_2_usuario.setText(self.usuario_pesquisado[0][3])
        self.cb_alterar_acesso_usuario.setCurrentText(self.usuario_pesquisado[0][4])

    def pesquisar_usuario(self):
        usuarioDAO = UsuariosDAO()
        valor_consulta = self.input_pesquisar_usuario.text().strip()

        resultado = usuarioDAO.pesquisar_usuario(valor_consulta)
        resultado = list(resultado)

        if valor_consulta != '':
            if not resultado:
                return QMessageBox.warning(QMessageBox(), 'Atenção', 'Usuário não encontrado!')
            else:
                self.tb_lista_usuarios.setRowCount(0)

                for idx_linha, linha in enumerate(resultado):
                    self.tb_lista_usuarios.insertRow(idx_linha)

                    for idx_coluna, coluna in enumerate(linha):
                        self.tb_lista_usuarios.setItem(idx_linha, idx_coluna, QTableWidgetItem(str(coluna)))
        else:
            return QMessageBox.warning(QMessageBox(), 'Atenção', 'Digite o valor da pesquisa!')

    def limpar_filtro_pesquisar(self):
        self.input_pesquisar_usuario.setText('')
        self.listar_todos_usuarios()



