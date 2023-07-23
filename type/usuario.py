import typing
import strawberry
from conn.db import conn
from models.index import usuarios
from models.index import estados
from strawberry.types import Info
from typing import Optional

lstEstados = conn.execute(estados.select()).fetchall()

@strawberry.type
class Estado:
    id: int
    nombre: str
    descripcion: str

@strawberry.type
class Usuario:
    id: int
    nombre: str
    correo: str
    idEstado: int
    @strawberry.field
    def estado(self, info: Info) -> Estado:  
        estado = next((estado for estado in lstEstados if estado.id == self.idEstado), None)
        if estado:
            return Estado(**dict(estado._mapping))
        else:
            return None
    
@strawberry.type
class Query:
    @strawberry.field
    def usuario(id: int) -> Optional[Usuario]:
        return conn.execute(usuarios.select().where(usuarios.c.id == id)).fetchone()
    @strawberry.field
    def usuario_por_correo(correo: str) -> Optional[Usuario]:
        query = usuarios.select().where(usuarios.c.correo == correo)
        return conn.execute(query).fetchone()
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
            "correo": correo
        }
        result = conn.execute(usuarios.insert(),usuario)
        conn.commit();
        return int(result.inserted_primary_key[0])
    @strawberry.mutation
    def update_usuario(self, id:int, nombre: str, correo: str, idEstado: int, info: Info) -> str:
        result = conn.execute(usuarios.update().where(usuarios.c.id == id), {
            "nombre": nombre,
            "correo": correo,
            "idEstado": idEstado
        })
        print(result. returns_rows)
        conn.commit();
        return str(result.rowcount) + " Row(s) updated"
    
    