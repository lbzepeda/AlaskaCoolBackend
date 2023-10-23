import typing
import strawberry
from conn.db import conn
from models.index import moneda

@strawberry.type
class Moneda:
    id: int
    nombre: str
    codigo: str
    idEstado: int

@strawberry.field
def moneda_por_id(id: int) -> Moneda:
    result = conn.execute(moneda.select().where(moneda.c.id == id)).fetchone()
    return result

@strawberry.field
def lista_moneda(self) -> typing.List[Moneda]:
    result = conn.execute(moneda.select()).fetchall()
    return result

lstMonedaQuery = [moneda_por_id, lista_moneda]