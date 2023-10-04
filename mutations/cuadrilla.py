import typing
import strawberry
from conn.db import conn, handle_db_transaction
from models.index import cuadrillas
from strawberry.types import Info

@strawberry.type
class Cuadrilla:
    id: int
    nombre: str
    descripcion: str

@strawberry.type
class Query:
    @strawberry.field
    def cuadrilla(id: int) -> Cuadrilla:
        return conn.execute(cuadrillas.select().where(cuadrillas.c.id == id)).fetchone()

    @strawberry.field
    def cuadrillas(self) -> typing.List[Cuadrilla]:
        return conn.execute(cuadrillas.select()).fetchall()


@strawberry.mutation
@handle_db_transaction
async def crear_cuadrilla(self, nombre: str, descripcion: str, info: Info) -> int:
    tipousuario = {
        "nombre": nombre,
        "descripcion": descripcion
    }
    result = conn.execute(cuadrillas.insert(), tipousuario)
    conn.commit()
    return int(result.inserted_primary_key[0])


@strawberry.mutation
@handle_db_transaction
def actualizar_cuadrilla(self, id: int, nombre: str, descripcion: str, info: Info) -> str:
    result = conn.execute(cuadrillas.update().where(cuadrillas.c.id == id), {
        "nombre": nombre,
        "descripcion": descripcion
    })
    print(result. returns_rows)
    conn.commit()
    return str(result.rowcount) + " Row(s) updated"


lstCuadrillaMutation = [crear_cuadrilla, actualizar_cuadrilla]
