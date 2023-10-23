import typing
import strawberry
from conn.db import conn
from models.index import contratacion_colaboradores, moneda, cargo, colaboradores, archivos
from datetime import datetime
from typing import Optional
from strawberry.types import Info
from .moneda import Moneda
from .cargo import Cargo
from .colaboradores import Colaboradores
from .archivos import Archivos

@strawberry.type
class ContratacionColaboradores:
    id: int
    SalarioBase: str
    idSalarioMoneda: int
    @strawberry.field
    def salariomoneda(self, info: Info) -> Optional[Moneda]:
        monedaresult = conn.execute(moneda.select().where(moneda.c.id == self.idSalarioMoneda)).first()
        return Moneda(**dict(monedaresult._mapping)) if monedaresult else None
    FechaInicio: datetime
    FechaFin: Optional[datetime]
    idCargo: Optional[int]
    @strawberry.field
    def cargo(self, info: Info) -> Optional[Cargo]:
        cargoresult = conn.execute(cargo.select().where(cargo.c.id == self.idCargo)).first()
        return Cargo(**dict(cargoresult._mapping)) if cargoresult else None
    idColaborador: int
    @strawberry.field
    def colaborador(self, info: Info) -> Optional[Colaboradores]:
        colaboradorresult = conn.execute(colaboradores.select().where(colaboradores.c.id == self.idColaborador)).first()
        return Colaboradores(**dict(colaboradorresult._mapping)) if colaboradorresult else None
    @strawberry.field
    def archivo(self, info: Info) -> typing.List[Optional[Archivos]]:  
        archivo_results = conn.execute(archivos.select().where(archivos.c.idContratacionesColaboradores == self.id)).fetchall()
        
        if archivo_results:
            return [Archivos(**dict(archivo._mapping)) for archivo in archivo_results]
        else:
            return None
    
    idEstado: int

@strawberry.field
def contratacion_colaborador_por_id(id: int) -> ContratacionColaboradores:
    result = conn.execute(contratacion_colaboradores.select().where(contratacion_colaboradores.c.id == id)).fetchone()
    return result

@strawberry.field
def lista_contratacion_colaborador(self) -> typing.List[ContratacionColaboradores]:
    result = conn.execute(contratacion_colaboradores.select()).fetchall()
    return result

lstContratacionColaboradoresQuery = [contratacion_colaborador_por_id, lista_contratacion_colaborador]