import typing
import strawberry
from conn.db import conn
from models.index import estados

@strawberry.type
class Estado:
    id: int
    nombre: str
    correo: str
@strawberry.type
class Query:
    @strawberry.field
    def estado(id: int) -> Estado:
        return conn.execute(estados.select().where(estados.c.id == id)).fetchone()
    @strawberry.field
    def estados(self) -> typing.List[Estado]:
        return conn.execute(estados.select()).fetchall()
