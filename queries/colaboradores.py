import typing
import strawberry
from conn.db import conn
from models.index import colaboradores, genero, estados
from datetime import datetime
from typing import Optional
from strawberry.types import Info
from .genero import Genero

lstGenero = conn.execute(genero.select()).fetchall()

@strawberry.type
class Colaboradores:
    id: int
    PrimerNombre: str
    SegundoNombre: str
    PrimerApellido: str
    SegundoApellido: str
    CorreoPersonal: str
    CorreoInstitucional: str
    FechaNacimiento: datetime
    idGenero: int
    @strawberry.field
    def genero(self, info: Info) -> Optional[Genero]:
        genero_object = next((Genero(**dict(g._mapping)) for g in lstGenero if g.id == self.idGenero), None)
        return genero_object
    idEstado: int

@strawberry.field
def colaborador_por_id(id: int) -> Colaboradores:
    result = conn.execute(colaboradores.select().where(colaboradores.c.id == id)).fetchone()
    return result

@strawberry.field
def lista_colaboradores(self) -> typing.List[Colaboradores]:
    result = conn.execute(colaboradores.select()).fetchall()
    return result

lstColaboradoresQuery = [colaborador_por_id, lista_colaboradores]