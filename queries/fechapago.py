import typing
import strawberry
from conn.db import conn
from typing import Optional
from strawberry.types import Info
from models.index import tipo_pago, esquema_pago
from datetime import datetime, time
from .esquemapago import EsquemaPago

@strawberry.type
class FechaPago:
    id: int
    fechainicio: datetime
    horainicio: time
    idesquemapago: int
    @strawberry.field
    def esquemapago(self, info: Info) -> Optional[EsquemaPago]:
        monedaresult = conn.execute(esquema_pago.select().where(esquema_pago.c.id == self.idesquemapago)).first()
        return EsquemaPago(**dict(monedaresult._mapping)) if monedaresult else None
    horafin: time

@strawberry.field
def fecha_pago_por_id(id: int) -> FechaPago:
    result = conn.execute(tipo_pago.select().where(tipo_pago.c.id == id)).fetchone()
    return result

@strawberry.field
def lista_fecha_pago(self) -> typing.List[FechaPago]:
    result = conn.execute(tipo_pago.select()).fetchall()
    return result

lstFechaPagoQuery = [fecha_pago_por_id, lista_fecha_pago]