import typing
import strawberry
from conn.db import conn
from models.index import esquema_pago, moneda, tipo_pago
from typing import Optional
from strawberry.types import Info
from .moneda import Moneda
from .tipopago import TipoPago

@strawberry.type
class EsquemaPago:
    id: int
    factorcalculo: Optional[str]
    monto: Optional[str]
    idmoneda: Optional[int]
    @strawberry.field
    def moneda(self, info: Info) -> Optional[Moneda]:
        monedaresult = conn.execute(moneda.select().where(moneda.c.id == self.idMoneda)).first()
        return Moneda(**dict(monedaresult._mapping)) if monedaresult else None
    idestado: int
    idtipopago: int
    @strawberry.field
    def tipopago(self, info: Info) -> Optional[TipoPago]:
        tipopagoresult = conn.execute(tipo_pago.select().where(tipo_pago.c.id == self.idTipoPago)).first()
        return TipoPago(**dict(tipopagoresult._mapping)) if tipopagoresult else None

@strawberry.field
def esquema_pago_por_id(id: int) -> EsquemaPago:
    result = conn.execute(esquema_pago.select().where(esquema_pago.c.id == id)).fetchone()
    return result

@strawberry.field
def lista_esquema_pago(self) -> typing.List[EsquemaPago]:
    result = conn.execute(esquema_pago.select()).fetchall()
    return result

lstEsquemaPagoQuery = [esquema_pago_por_id, lista_esquema_pago]