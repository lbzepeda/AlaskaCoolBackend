import typing
import strawberry
from conn.db import conn
from models.index import bancos

@strawberry.type
class Banco:
    id: int
    nombre: str
    descripcion: str

@strawberry.field
def banco_por_id(id: int) -> Banco:
    result = conn.execute(bancos.select().where(bancos.c.id == id)).fetchone()
    return result

@strawberry.field
def lista_bancos(self) -> typing.List[Banco]:
    result = conn.execute(bancos.select()).fetchall()
    return result

lstBancoQuery = [banco_por_id, lista_bancos]