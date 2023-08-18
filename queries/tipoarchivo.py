import typing
import strawberry
from conn.db import conn
from models.index import tipo_archivo

@strawberry.type
class TipoArchivo:
    id: int
    nombre: str
    descripcion: str

@strawberry.field
def tipo_archivo_por_id(id: int) -> TipoArchivo:
    result = conn.execute(tipo_archivo.select().where(tipo_archivo.c.id == id)).fetchone()
    conn.commit()
    return result

@strawberry.field
def lista_tipos_archivo(self) -> typing.List[TipoArchivo]:
    result = conn.execute(tipo_archivo.select()).fetchall()
    conn.commit()
    return result

lstTipoArchivoQuery = [tipo_archivo_por_id, lista_tipos_archivo]