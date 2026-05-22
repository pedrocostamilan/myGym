class Serie:
    def __init__(self, id: int, sessao_id: int, exercicio_id: int, qtd_series: int, reps: int, carga: float):
        self.id = id
        self.sessao_id = sessao_id
        self.exercicio_id = exercicio_id
        self.qtd_series = qtd_series
        self.reps = reps
        self.carga = carga