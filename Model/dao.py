import sqlite3

class DAO():
    def __init__(self, name='banco_inovafactory.db') -> None:
        self.name = name

    def abre_conexao(self):
        self.conexao = sqlite3.connect(self.name)

    def fecha_conexao(self):
        try:
            self.conexao.close()
        except:
            pass

if __name__ == '__main__':
    db = DAO()
    db.abre_conexao()
    db.fecha_conexao()
