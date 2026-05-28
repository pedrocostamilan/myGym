from database.connection import Connection
from database.crud import dbCrud

DATABASE = Connection("database.sqlite")
CRUD = dbCrud("database.sqlite")

CRUD.criaExercicio("Supino reto", "Peitoral maior")
CRUD.criaExercicio("Elevação lateral", "Deltoide(lateral)")
CRUD.criaTreino("Push", "Treino com 3 exercícios para peitoral, 2 para tríceps e 2 de ombro + abs se possível")
CRUD.criaSessao(1, "25-05-2026")