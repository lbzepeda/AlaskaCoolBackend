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
@strawberry.type
class Query:
    @strawberry.field
    def cuadrilla(id: int) -> Cuadrilla:
        return conn.execute(cuadrillas.select().where(cuadrillas.c.id == id)).fetchone()
    @strawberry.field
    def cuadrillas(self) -> typing.List[Cuadrilla]:
        return conn.execute(cuadrillas.select()).fetchall()
@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_cuadrilla(self, nombre: str, descripcion: str, info: Info) -> int:
        tipousuario =  {
            "nombre": nombre,
            "descripcion": descripcion
        }
        result = conn.execute(cuadrillas.insert(),tipousuario)
        conn.commit();
        return int(result.inserted_primary_key[0])
    @strawberry.mutation
    def update_cuadrilla(self, id:int, nombre: str, descripcion: str, info: Info) -> str:
        result = conn.execute(cuadrillas.update().where(cuadrillas.c.id == id), {
            "nombre": nombre,
            "descripcion": descripcion
        })
        print(result. returns_rows)
        conn.commit();
        return str(result.rowcount) + " Row(s) updated"
    