import typing
import strawberry
from conn.db import conn
from models.index import genero

@strawberry.type
class Genero:
    id: int
    nombre: str
    descripcion: str

@strawberry.field
def genero_por_id(id: int) -> Genero:
    result = conn.execute(genero.select().where(genero.c.id == id)).fetchone()
    return result

@strawberry.field
def lista_genero(self) -> typing.List[Genero]:
    result = conn.execute(genero.select()).fetchall()
    return result

lstGeneroQuery = [genero_por_id, lista_genero]