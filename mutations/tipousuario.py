import strawberry
from conn.db import conn, handle_db_transaction
from models.index import tipo_usuario
from strawberry.types import Info

@strawberry.type
class TipoUsuario:
    id: int
    nombre: str
    descripcion: str

@strawberry.mutation
@handle_db_transaction
def crear_tipo_usuario(self, nombre: str, descripcion: str, info: Info) -> int:
    tipousuario =  {
        "nombre": nombre,
        "descripcion": descripcion
    }
    result = conn.execute(tipo_usuario.insert(),tipousuario)
    conn.commit()
    return int(result.inserted_primary_key[0])

@strawberry.mutation
@handle_db_transaction
def actualizar_tipo_usuario(self, id:int, nombre: str, descripcion: str, info: Info) -> str:
    result = conn.execute(tipo_usuario.update().where(tipo_usuario.c.id == id), {
        "nombre": nombre,
        "descripcion": descripcion
    })
    print(result. returns_rows)
    conn.commit()
    return str(result.rowcount) + " Row(s) updated"

lstTipoUsuarioMutation = [crear_tipo_usuario, actualizar_tipo_usuario]