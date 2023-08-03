import typing
import strawberry
from conn.db import conn
from models.index import usuario_cuadrilla
from strawberry.types import Info
from models.index import usuarios
from models.cuadrilla import cuadrillas
from typing import Optional
from .usuario import Usuario
from .cuadrilla import Cuadrilla

lstUsuarios = conn.execute(usuarios.select()).fetchall()
lstCuadrillas= conn.execute(cuadrillas.select()).fetchall()

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
        
@strawberry.field
def usuario_cuadrilla_por_id(id: int) -> UsuarioCuadrilla:
    return conn.execute(usuario_cuadrilla.select().where(usuario_cuadrilla.c.id == id)).fetchone()
@strawberry.field
def lista_usuario_cuadrilla(self) -> typing.List[UsuarioCuadrilla]:
    return conn.execute(usuario_cuadrilla.select()).fetchall()

lstUsuarioCuadrillaQuery = [usuario_cuadrilla_por_id, lista_usuario_cuadrilla]