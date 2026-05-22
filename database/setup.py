import sqlite3

class Setup:

    def __init__(self, db_nome="banco.db"):
        self.db_nome = db_nome
        self.connection = sqlite3.connect(db_nome, check_same_thread=False)
        self.setupTables

    def __setupTables(self):
        cur = self.connection.cursor()

        cur = cur.execute('''


        ''')
