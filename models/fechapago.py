from conn.db import meta
from sqlalchemy import ForeignKey
from sqlalchemy import Table, Column, Integer, DateTime, String
from sqlalchemy.sql.sqltypes import Integer

fecha_pago = Table('fecha_pago', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('FechaInicio', DateTime, nullable=False),
    Column('idEsquemaPago', Integer, ForeignKey('esquema_pago.id')),
    Column('idEstado', Integer, ForeignKey('estados.id')),
)