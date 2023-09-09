import typing
import strawberry
from conn.db import conn
from models.index import tipo_usuario

@strawberry.type
class TipoUsuario:
    id: int
    nombre: str
    descripcion: str

@strawberry.field
def tipo_usuario_por_id(id: int) -> TipoUsuario:
    result = conn.execute(tipo_usuario.select().where(tipo_usuario.c.id == id)).fetchone()
    return result

@strawberry.field
def lista_tipos_usuario(self) -> typing.List[TipoUsuario]:
    result = conn.execute(tipo_usuario.select()).fetchall()
    return result

lstTipoUsuarioQuery = [tipo_usuario_por_id, lista_tipos_usuario]