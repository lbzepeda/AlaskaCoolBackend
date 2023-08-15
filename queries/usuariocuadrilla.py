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

@strawberry.type
class UsuarioCuadrilla:
    id: int
    idUsuario: int
    @strawberry.field
    def usuario(self, info: Info) -> Optional[Usuario]:  
        lstUsuarios = conn.execute(usuarios.select()).fetchall()
        matched_usuario = next((usuario for usuario in lstUsuarios if usuario.id == self.idUsuario), None)
        if matched_usuario:
            return Usuario(**dict(matched_usuario._mapping))
        return None
    idCuadrilla: int
    @strawberry.field
    def cuadrilla(self, info: Info) -> Optional[Cuadrilla]:  
        lstCuadrillas = conn.execute(cuadrillas.select()).fetchall()
        matched_cuadrilla = next((cuadrilla for cuadrilla in lstCuadrillas if cuadrilla.id == self.idCuadrilla), None)
        if matched_cuadrilla:
            return Cuadrilla(**dict(matched_cuadrilla._mapping))
        return None
        
@strawberry.field
def usuario_cuadrilla_por_id(id: int) -> UsuarioCuadrilla:
    result = conn.execute(usuario_cuadrilla.select().where(usuario_cuadrilla.c.id == id)).fetchone()
    conn.commit()
    return result

@strawberry.field
def lista_usuario_cuadrilla(self) -> typing.List[UsuarioCuadrilla]:
    result = conn.execute(usuario_cuadrilla.select()).fetchall()
    conn.commit()
    return result

lstUsuarioCuadrillaQuery = [usuario_cuadrilla_por_id, lista_usuario_cuadrilla]