import typing
import strawberry
from conn.db import conn
from models.index import tipo_pago

@strawberry.type
class TipoPago:
    id: int
    nombre: str
    descripcion: str 

@strawberry.field
def tipo_pago_por_id(id: int) -> TipoPago:
    result = conn.execute(tipo_pago.select().where(tipo_pago.c.id == id)).fetchone()
    return result

@strawberry.field
def lista_tipo_pago(self) -> typing.List[TipoPago]:
    result = conn.execute(tipo_pago.select()).fetchall()
    return result

lstTipoPagoQuery = [tipo_pago_por_id, lista_tipo_pago]