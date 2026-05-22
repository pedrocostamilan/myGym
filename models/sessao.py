from datetime import date

class Sessao:
    def __init__(self, id: int, treino_id: int, data_exec: date):
        self.id = id
        self.treino_id = treino_id
        self.data_exec = data_exec