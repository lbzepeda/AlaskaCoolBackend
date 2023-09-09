import typing
import strawberry
from conn.db import conn
from models.index import estado_programacion

@strawberry.type
class EstadoProgramacion:
    id: int
    nombre: str
    descripcion: str

@strawberry.field
def estado_programacion_por_id(id: int) -> EstadoProgramacion:
    result = conn.execute(estado_programacion.select().where(estado_programacion.c.id == id)).fetchone()
    return result

@strawberry.field
def lista_estado_programacion(self) -> typing.List[EstadoProgramacion]:
    result = conn.execute(estado_programacion.select()).fetchall()
    return result

lstEstadoProgramacionQuery = [estado_programacion_por_id, lista_estado_programacion]