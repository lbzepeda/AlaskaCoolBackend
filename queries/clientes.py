import typing
import strawberry
from conn.db import conn_sql
from models.index import clientes
from strawberry.types import Info
from typing import Optional
from datetime import datetime
from decimal import Decimal

@strawberry.type
class Clientes:
    CodCliente: str
    Nombres: str
    Apellidos: str
    RazonSocial: str
    Direccion: str
    Telefonos: str
    FAX: str
    Celular: str
    WebPage: Optional[str]
    Distrito: str
    Barrio: str
    CodTipoCliente: str
    CodVendedor: Optional[str]
    CodSupervisor: str

@strawberry.field
def cliente_por_id(CodCliente: str) -> Optional[Clientes]:
    result = conn_sql.execute(clientes.select().where(clientes.c.CodCliente == CodCliente)).fetchone()
    return result

@strawberry.field
def lista_clientes(self) -> typing.List[Clientes]:
    result = conn_sql.execute(clientes.select()).fetchall()
    return result

lstClienteQuery = [cliente_por_id, lista_clientes]