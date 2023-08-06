import typing
import strawberry
from conn.db import conn
from models.index import cuadrillas
from strawberry.types import Info

@strawberry.type
class Cuadrilla:
    id: int
    nombre: str
    descripcion: str

@strawberry.field
def cuadrilla_por_id(id: int) -> Cuadrilla:
    result = conn.execute(cuadrillas.select().where(cuadrillas.c.id == id)).fetchone()
    conn.commit()
    return result
@strawberry.field
def lista_cuadrilla(self) -> typing.List[Cuadrilla]:
    result = conn.execute(cuadrillas.select()).fetchall()
    conn.commit()
    return result

lstCuadrillaQuery = [cuadrilla_por_id, lista_cuadrilla]