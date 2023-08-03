import typing
import strawberry
from conn.db import conn
from models.index import usuarios
from models.index import estados
from models.index import tipo_usuario
from strawberry.types import Info
from typing import Optional


@strawberry.mutation
async def crear_usuario(self, nombre: str, correo: str, idTipoUsuario: int, info: Info) -> int:
    usuario =  {
        "nombre": nombre,
        "correo": correo,
        "idTipoUsuario": idTipoUsuario,
    }
    result = conn.execute(usuarios.insert(),usuario)
    conn.commit();
    return int(result.inserted_primary_key[0])
@strawberry.mutation
def actualizar_usuario(self, id:int, nombre: str, correo: str, idEstado: int, idTipoUsuario: int,info: Info) -> str:
    result = conn.execute(usuarios.update().where(usuarios.c.id == id), {
        "nombre": nombre,
        "correo": correo,
        "idEstado": idEstado,
        "idTipoUsuario": idTipoUsuario,
    })
    print(result. returns_rows)
    conn.commit();
    return str(result.rowcount) + " Row(s) updated"

lstUsuarioMutation = [crear_usuario, actualizar_usuario]