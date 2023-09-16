import typing
import strawberry
from conn.db import conn
from strawberry.types import Info
from typing import Optional
from models.index import archivo_programacion
from models.index import tipo_archivo
from .tipoarchivo import *

@strawberry.type
class ArchivoProgramacion:
    id: int
    PathArchivo: str
    idTipoArchivo: int
    @strawberry.field
    def tipoarchivo(self, info: Info) -> typing.List[Optional[TipoArchivo]]:
        current_det_proformas = conn.execute(tipo_archivo.select()).fetchall()

        matched_proformas = [
            TipoArchivo(**dict(det._mapping))
            for det in current_det_proformas 
            if det.id == self.idTipoArchivo
        ]
        return matched_proformas or []
    idProgramacion: int
    NombreArchivo: str

@strawberry.field
def archivo_programacion_por_id(id: int) -> typing.List[ArchivoProgramacion]:
    result = conn.execute(archivo_programacion.select().where(archivo_programacion.c.idProgramacion == id)).fetchall()
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