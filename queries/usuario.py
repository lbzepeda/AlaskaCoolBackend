import strawberry
from typing import Optional
from conn.db import conn
import typing
from models.index import usuarios
from models.index import estados
from models.index import tipo_usuario
import strawberry
from strawberry.types import Info

lstEstados = conn.execute(estados.select()).fetchall()
lstTipoUsuario = conn.execute(tipo_usuario.select()).fetchall()

@strawberry.type
class TipoUsuario:
    id: int
    nombre : str
    descripcion: str

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
        tipoUsuario = next((tipoUsuario for tipoUsuario in lstTipoUsuario if tipoUsuario.id == self.idTipoUsuario), None)
        if tipoUsuario:
            return TipoUsuario(**dict(tipoUsuario._mapping))
        else:
            return None
    idEstado: int
    @strawberry.field
    def estado(self, info: Info) -> Estado:  
        estado = next((estado for estado in lstEstados if estado.id == self.idEstado), None)
        if estado:
            return Estado(**dict(estado._mapping))
        else:
            return None

@strawberry.field
def lista_usuario_por_id(id: int) -> Optional[Usuario]:
    return conn.execute(usuarios.select().where(usuarios.c.id == id)).fetchone()
@strawberry.field
def usuario_por_correo(correo: str) -> Optional[Usuario]:
    query = usuarios.select().where(usuarios.c.correo == correo)
    return conn.execute(query).fetchone()
@strawberry.field
def lista_usuario(self) -> typing.List[Usuario]:
    return conn.execute(usuarios.select()).fetchall()

lstUsuarioQuery = [lista_usuario_por_id, usuario_por_correo, lista_usuario]