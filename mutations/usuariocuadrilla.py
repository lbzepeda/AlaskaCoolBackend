import typing
import strawberry
from conn.db import conn, handle_db_transaction
from models.index import usuario_cuadrilla
from strawberry.types import Info
from models.index import usuarios
from models.cuadrilla import cuadrillas
from typing import Optional

@strawberry.mutation
@handle_db_transaction
async def create_usuario_cuadrilla(self, idUsuario: int, idCuadrilla: int, info: Info) -> int:
    tipousuario =  {
        "idUsuario": idUsuario,
        "idCuadrilla": idCuadrilla
    }
    result = conn.execute(usuario_cuadrilla.insert(),tipousuario)
    conn.commit()
    return int(result.inserted_primary_key[0])

@strawberry.mutation
@handle_db_transaction
def actualizar_usuario_cuadrilla(self, id:int, idUsuario: int, idCuadrilla: int, info: Info) -> str:
    result = conn.execute(usuario_cuadrilla.update().where(usuario_cuadrilla.c.id == id), {
        "idUsuario": idUsuario,
        "idCuadrilla": idCuadrilla
    })
    print(result. returns_rows)
    conn.commit()
    return str(result.rowcount) + " Row(s) updated"

lstUsuarioCuadrillaMutation = [create_usuario_cuadrilla, actualizar_usuario_cuadrilla]