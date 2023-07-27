import typing
import strawberry
from conn.db import conn
from models.index import usuario_cuadrilla
from strawberry.types import Info
from models.index import usuarios
from models.cuadrilla import cuadrillas
from typing import Optional

lstUsuarios = conn.execute(usuarios.select()).fetchall()
lstCuadrillas= conn.execute(cuadrillas.select()).fetchall()

@strawberry.type
class Usuario:
    id: int
    nombre: str
    correo: str
    idEstado: int
    idTipoUsuario: int

@strawberry.type
class Cuadrilla:
    id: int
    nombre: str
    descripcion: str

@strawberry.type
class UsuarioCuadrilla:
    id: int
    idUsuario: int
    @strawberry.field
    def usuario(self, info: Info) -> Optional[Usuario]:  
        usuario = next((usuario for usuario in lstUsuarios if usuario.id == self.idUsuario), None)
        if usuario:
            return Usuario(**dict(usuario._mapping))
        else:
            return None
    idCuadrilla: int
    @strawberry.field
    def cuadrilla(self, info: Info) -> Optional[Cuadrilla]:  
        cuadrilla = next((cuadrillas for cuadrillas in lstCuadrillas if cuadrillas.id == self.idCuadrilla), None)
        if cuadrilla:
            return Cuadrilla(**dict(cuadrilla._mapping))
        else:
            return None

@strawberry.type
class Query:
    @strawberry.field
    def usuariocuadrilla(id: int) -> UsuarioCuadrilla:
        return conn.execute(usuario_cuadrilla.select().where(usuario_cuadrilla.c.id == id)).fetchone()
    @strawberry.field
    def usuariocuadrillas(self) -> typing.List[UsuarioCuadrilla]:
        return conn.execute(usuario_cuadrilla.select()).fetchall()
    
@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_usuario_cuadrilla(self, idUsuario: int, idCuadrilla: int, info: Info) -> int:
        tipousuario =  {
            "idUsuario": idUsuario,
            "idCuadrilla": idCuadrilla
        }
        result = conn.execute(usuario_cuadrilla.insert(),tipousuario)
        conn.commit();
        return int(result.inserted_primary_key[0])
    @strawberry.mutation
    def update_usuario_cuadrilla(self, id:int, idUsuario: int, idCuadrilla: int, info: Info) -> str:
        result = conn.execute(usuario_cuadrilla.update().where(usuario_cuadrilla.c.id == id), {
            "idUsuario": idUsuario,
            "idCuadrilla": idCuadrilla
        })
        print(result. returns_rows)
        conn.commit();
        return str(result.rowcount) + " Row(s) updated"
    
