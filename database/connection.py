import sqlite3

class Connection:

    def __init__(self, db_nome="banco.db"):
        self.db_nome = db_nome
        self.connection = sqlite3.connect(db_nome, check_same_thread=False)
        self.setupTables()

    def setupTables(self):
        cur = self.connection.cursor()

        #Tabela treino
        cur.execute('''
            CREATE TABLE IF NOT EXISTS treino (
                treino_id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(150) NOT NULL,
                descricao TEXT
            )
        ''')

        #Tabela exercicio
        cur.execute('''
            CREATE TABLE IF NOT EXISTS exercicio (
                exercicio_id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(150) NOT NULL,
                grupo_muscular VARCHAR(100)
            )
        ''')

        #Tabela que liga que exercícios pertencem a que treinos
        cur.execute('''
            CREATE TABLE IF NOT EXISTS treino_exercicio (
                treino_exercicio_id INTEGER PRIMARY KEY AUTOINCREMENT,
                treino_id INTEGER NOT NULL,
                exercicio_id INTEGER NOT NULL,
                FOREIGN KEY (treino_id) REFERENCES treino (treino_id),
                FOREIGN KEY (exercicio_id) REFERENCES exercicio (exercicio_id)
            )
        ''')

        #Tabela sessão (dia que o treino foi executado)
        cur.execute('''
            CREATE TABLE IF NOT EXISTS sessao (
                session_id INTEGER PRIMARY KEY AUTOINCREMENT,
                treino_id INTEGER NOT NULL,
                data_exec DATETIME NOT NULL,
                FOREIGN KEY (treino_id) REFERENCES treino (treino_id)
            )
        ''')

        #Correção Nestor
        # Agora ela interage com o contexto do dia (session_id) e o exercício (exercicio_id)
        cur.execute('''
            CREATE TABLE IF NOT EXISTS serie (
                serie_id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id INTEGER NOT NULL,
                exercicio_id INTEGER NOT NULL,
                repeticoes INTEGER NOT NULL,
                carga REAL NOT NULL,
                FOREIGN KEY (session_id) REFERENCES sessao (session_id),
                FOREIGN KEY (exercicio_id) REFERENCES exercicio (exercicio_id)
            )
        ''')

        self.connection.commit()