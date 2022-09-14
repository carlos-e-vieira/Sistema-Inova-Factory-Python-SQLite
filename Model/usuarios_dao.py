from Model.dao import DAO

class UsuariosDAO():
    def cadastrar_usuario(self, nome, login, senha, acesso):
        try:
            dao = DAO()
            dao.abre_conexao()
            cursor = dao.conexao.cursor()
            cursor.execute("""

                INSERT INTO usuarios(nome_usuario, login_usuario, senha_usuario, acesso_usuario) VALUES(?, ?, ?, ?)

            """, (nome, login, senha, acesso))
            dao.conexao.commit()
            dao.fecha_conexao()
        except AttributeError:
            print('Erro ao inserir dados.')

    def listar_todos_usuarios(self):
        try:
            dao = DAO()
            dao.abre_conexao()
            cursor = dao.conexao.cursor()
            cursor.execute("SELECT * FROM usuarios ORDER BY id_usuario")
            usuarios = cursor.fetchall()
            return usuarios
        except:
            pass

    def excluir_usuario(self, id):
        try:
            dao = DAO()
            dao.abre_conexao()
            cursor = dao.conexao.cursor()
            cursor.execute(f"DELETE FROM usuarios WHERE id_usuario = '{id}' ")
            dao.conexao.commit()
            dao.fecha_conexao()

            return 'Usuário excluido com sucesso'
        except:
            return 'Erro ao excluir'

    def atualizar_usuario(self, id, nome, login, senha, acesso):
        dao = DAO()
        dao.abre_conexao()
        cursor = dao.conexao.cursor()
        cursor.execute(f"UPDATE usuarios SET nome_usuario = '{nome}', login_usuario = '{login}', senha_usuario = '{senha}', acesso_usuario = '{acesso}' WHERE id_usuario = '{id}'")

        dao.conexao.commit()
        dao.fecha_conexao()

    def listar_usuario(self, id):
        try:
            dao = DAO()
            dao.abre_conexao()
            cursor = dao.conexao.cursor()
            cursor.execute(f"SELECT * FROM usuarios WHERE id_usuario = {id}")
            usuario = cursor.fetchall()
            return usuario
        except:
            pass


    def pesquisar_usuario(self, filtro):
        try:
            dao = DAO()
            dao.abre_conexao()
            cursor = dao.conexao.cursor()
            cursor.execute(f"SELECT * FROM usuarios WHERE nome_usuario LIKE '%{filtro}%'")
            usuario = cursor.fetchall()
            return usuario
        except:
            pass