import typing
import strawberry
from conn.db import conn
from models.index import tipo_programacion

@strawberry.type
class TipoProgramacion:
    id: int
    nombre: str
    descripcion: str

@strawberry.field
def tipo_programacion_por_id(id: int) -> TipoProgramacion:
    result = conn.execute(tipo_programacion.select().where(tipo_programacion.c.id == id)).fetchone()
    return result

@strawberry.field
def lista_tipos_programacion(self) -> typing.List[TipoProgramacion]:
    result = conn.execute(tipo_programacion.select()).fetchall()
    return result

lstTipoProgramacionQuery = [tipo_programacion_por_id, lista_tipos_programacion]