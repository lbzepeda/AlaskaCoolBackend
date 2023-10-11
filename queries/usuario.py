import strawberry
from typing import Optional
from conn.db import conn
import typing
import sqlalchemy
from models.index import usuarios
from models.index import estados
from models.index import tipo_usuario
import strawberry
from strawberry.types import Info
from .tipousuario import TipoUsuario

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
    idTipoUsuario: int
    @strawberry.field
    def tipo_usuario(self, info: Info) -> TipoUsuario:
        current_tipoUsuarios = conn.execute(tipo_usuario.select()).fetchall()
        
        tipoUsuario = next(
            (tipoUsuario for tipoUsuario in current_tipoUsuarios if tipoUsuario.id == self.idTipoUsuario), 
            None
        )
        if tipoUsuario:
            return TipoUsuario(**dict(tipoUsuario._mapping))
        return None
    idEstado: int
    @strawberry.field
    def estado(self, info: Info) -> Estado:  
        current_estados = conn.execute(estados.select()).fetchall()
        
        estado = next(
            (estado for estado in current_estados if estado.id == self.idEstado),
            None
        )
        if estado:
            return Estado(**dict(estado._mapping))
        return None

@strawberry.field
def usuario_por_id(id: int) -> Optional[Usuario]:
    result = conn.execute(usuarios.select().where(usuarios.c.id == id)).fetchone()
    return result

@strawberry.field
def usuario_por_correo(correo: str) -> Optional[Usuario]:
    result = conn.execute(usuarios.select().where(usuarios.c.correo == correo)).fetchone()
    return result

@strawberry.field
def lista_usuario(self) -> typing.List[Usuario]:
    result = conn.execute(usuarios.select()).fetchall()
    return result

@strawberry.field
def lista_usuarios_tecnicos(self) -> typing.List[Usuario]:
    result = conn.execute(usuarios.select().where(usuarios.c.idTipoUsuario.in_([1, 2, 5]))).fetchall()
    return result

@strawberry.field
def lista_usuarios_sistema(self) -> typing.List[Usuario]:
    result = conn.execute(
        usuarios.select().where(
            sqlalchemy.and_(
                usuarios.c.idTipoUsuario.in_([3, 4, 5, 6, 7]),
                usuarios.c.idEstado == 1
            )
        )
    ).fetchall()
    return result

lstUsuarioQuery = [usuario_por_id, usuario_por_correo, lista_usuario, lista_usuarios_tecnicos, lista_usuarios_sistema]