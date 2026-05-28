import sqlite3
from datetime import date

class dbCrud:

    def __init__(self, db_nome="database.sqlite"):
        self.db_nome = db_nome
        self.connection = sqlite3.connect(db_nome, check_same_thread=False)

    def criaTreino(self, nome: str, descricao: str):
        cur = self.connection.cursor()

        cur.execute(
            "INSERT INTO treino (nome, descricao) VALUES (?, ?)",
            (nome, descricao)
        )
        self.connection.commit()


    def criaExercicio(self, nome: str, grupo_muscular: str):
        cur = self.connection.cursor()

        cur.execute(
            "INSERT INTO exercicio (nome, grupo_muscular) VALUES (?, ?)",
            (nome, grupo_muscular)  
        )
        self.connection.commit()

    def criaSessao(self, treino_id: int, data_exec: date):
        cur = self.connection.cursor()
        
        cur.execute(
            "INSERT INTO sessao (treino_id, data_exec) VALUES (?, ?)",
            (treino_id, data_exec)
        )
        self.connection.commit()