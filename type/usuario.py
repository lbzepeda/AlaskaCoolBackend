import typing
import strawberry
from conn.db import conn
from models.index import usuarios
from strawberry.types import Info

@strawberry.type
class Usuario:
    id: int
    nombre: str
    correo: str
@strawberry.type
class Query:
    @strawberry.field
    def usuario(id: int) -> Usuario:
        return conn.execute(usuarios.select().where(usuarios.c.id == id)).fetchone()
    @strawberry.field
    def usuarios(self) -> typing.List[Usuario]:
        return conn.execute(usuarios.select()).fetchall()

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_flavour(self, nombre: str, info: Info) -> bool:
        return True
    @strawberry.mutation
    async def create_usuario(self, nombre: str, correo: str, info: Info) -> int:
        usuario =  {
            "nombre": nombre,
            "correo": correo,
        }
        result = conn.execute(usuarios.insert(),usuario)
        conn.commit();
        return int(result.inserted_primary_key[0])
    @strawberry.mutation
    def update_usuario(self, id:int, nombre: str, correo: str, info: Info) -> str:
        result = conn.execute(usuarios.update().where(usuarios.c.id == id), {
            "nombre": nombre,
            "correo": correo
        })
        print(result. returns_rows)
        conn.commit();
        return str(result.rowcount) + " Row(s) updated"
    @strawberry.mutation
    def delete_usuario(self, id: int) -> bool:
        result = conn.execute(usuarios.delete().where(usuarios.c.id == id))
        return result.rowcount > 0
    
    