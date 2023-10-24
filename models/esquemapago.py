from conn.db import meta
from sqlalchemy import ForeignKey
from sqlalchemy import Table, Column, Integer, DateTime, String
from sqlalchemy.sql.sqltypes import Integer

esquema_pago = Table('esquema_pago', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('FactorCalculo', String(50)),
    Column('Monto', String(50)),
    Column('idMoneda', Integer, ForeignKey('moneda.id')),
    Column('idEstado', Integer, ForeignKey('estados.id')),
    Column('idTipoPago', Integer, ForeignKey('tipo_pago.id')),
)