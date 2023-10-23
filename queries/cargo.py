import typing
import strawberry
from conn.db import conn
from models.index import cargo

@strawberry.type
class Cargo:
    id: int
    nombre: str
    descripcion: str
    responsabilidades: str
    idEstado: int

@strawberry.field
def cargo_por_id(id: int) -> Cargo:
    result = conn.execute(cargo.select().where(cargo.c.id == id)).fetchone()
    return result

@strawberry.field
def lista_cargos(self) -> typing.List[Cargo]:
    result = conn.execute(cargo.select()).fetchall()
    return result

lstCargoQuery = [cargo_por_id, lista_cargos]