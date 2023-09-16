import typing
import strawberry
from conn.db import conn
from models.index import archivo_programacion

@strawberry.type
class ArchivoProgramacion:
    id: int
    PathArchivo: str
    idTipoArchivo: int
    idProgramacion: int
    NombreArchivo: str

@strawberry.field
def archivo_programacion_por_id(id: int) -> ArchivoProgramacion:
    result = conn.execute(archivo_programacion.select().where(archivo_programacion.c.id == id)).fetchone()
    return result

@strawberry.field
def lista_archivo_programacion(self) -> typing.List[ArchivoProgramacion]:
    result = conn.execute(archivo_programacion.select()).fetchall()
    return result

@strawberry.field
def cantidad_archivos_por_id(id: int) -> int:
    result = conn.execute(archivo_programacion.select().where(archivo_programacion.c.idProgramacion == id)).fetchall()
    return len(result)


lstArchivoProgramacionQuery = [archivo_programacion_por_id, lista_archivo_programacion, cantidad_archivos_por_id]