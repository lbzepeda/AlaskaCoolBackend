import typing
import strawberry
from conn.db import conn
from models.index import archivos
from typing import Optional
from strawberry.types import Info
from models.index import tipo_archivo
from .tipoarchivo import *

@strawberry.type
class Estado:
    id: int
    nombre: str
    descripcion: str

@strawberry.type
class Archivos:
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
    NombreArchivo: str
    idContratacionesColaboradores: int

@strawberry.field
def archivo_por_id(id: int) -> Archivos:
    result = conn.execute(archivos.select().where(archivos.c.id == id)).fetchone()
    return result

@strawberry.field
def lista_archivo(self) -> typing.List[Archivos]:
    result = conn.execute(archivos.select()).fetchall()
    return result

lstTipoArchivoQuery = [archivo_por_id, lista_archivo]