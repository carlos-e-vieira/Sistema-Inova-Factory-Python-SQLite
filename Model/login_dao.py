from Model.dao import DAO

class LoginDAO():
    def verifica_usuario(self, login, senha):
        try:
            dao = DAO()
            dao.abre_conexao()
            cursor = dao.conexao.cursor()
            cursor.execute("""
    
                SELECT * FROM usuarios
    
            """)

            for linha in cursor.fetchall():
                if linha[2].upper() == login.upper() and linha[3] == senha and linha[4] == 'Administrador':
                    return 'Administrador'
                elif linha[2].upper() == login.upper() and linha[3] == senha and linha[4] == 'Usuário':
                    return 'Usuário'
                else:
                    continue
            return 'sem acesso'

        except:
            pass

