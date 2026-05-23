import sqlite3

class Setup:

    def __init__(self, db_nome="banco.db"):
        self.db_nome = db_nome
        self.connection = sqlite3.connect(db_nome, check_same_thread=False)
        self.setupTables()

    def setupTables(self):
        cur = self.connection.cursor()

        cur.execute('''
        CREATE TABLE IF NOT EXISTS exercicio (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL UNIQUE,
            grupo_muscular TEXT NOT NULL
            )
        ''')

        cur.execute('''
        CREATE TABLE IF NOT EXISTS treino (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            descricao TEXT
            )
        ''')

        cur.execute('''
        CREATE TABLE IF NOT EXISTS sessao (
            id INTEGER PRIMARY KEY,
            treino_id INTEGER NOT NULL,
            data_exec TEXT NOT NULL,
                    
            FOREIGN KEY (treino_id) REFERENCES treino(id)
            )
        ''')

        cur.execute('''
        CREATE TABLE IF NOT EXISTS serie (
            id INTEGER PRIMARY KEY,
            sessao_id INTEGER NOT NULL, 
            exercicio_id INTEGER NOT NULL,
            qtd_series INTEGER NOT NULL,
            reps INTEGER NOT NULL, 
            carga REAL NOT NULL,
                    
            FOREIGN KEY (sessao_id) REFERENCES sessao(id),
            FOREIGN KEY (exercicio_id) REFERENCES exercicio(id)
            )
        ''')
        self.connection.commit()