import typing
import strawberry
from conn.db import conn
from models.index import tipo_usuario
from strawberry.types import Info

@strawberry.type
class TipoUsuario:
    id: int
    nombre: str
    descripcion: str
@strawberry.type
class Query:
    @strawberry.field
    def tipousuario(id: int) -> TipoUsuario:
        return conn.execute(tipo_usuario.select().where(tipo_usuario.c.id == id)).fetchone()
    @strawberry.field
    def tipousuarios(self) -> typing.List[TipoUsuario]:
        return conn.execute(tipo_usuario.select()).fetchall()
    
@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_flavour(self, nombre: str, info: Info) -> bool:
        return True
    @strawberry.mutation
    async def create_tipo_usuario(self, nombre: str, descripcion: str, info: Info) -> int:
        tipousuario =  {
            "nombre": nombre,
            "descripcion": descripcion
        }
        result = conn.execute(tipo_usuario.insert(),tipousuario)
        conn.commit();
        return int(result.inserted_primary_key[0])
    @strawberry.mutation
    def update_tipo_usuario(self, id:int, nombre: str, descripcion: str, info: Info) -> str:
        result = conn.execute(tipo_usuario.update().where(tipo_usuario.c.id == id), {
            "nombre": nombre,
            "descripcion": descripcion
        })
        print(result. returns_rows)
        conn.commit();
        return str(result.rowcount) + " Row(s) updated"
    
