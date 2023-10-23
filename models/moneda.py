from conn.db import meta
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy import ForeignKey

moneda = Table('moneda', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('nombre', String(50)),
    Column('codigo', String(50)),
    Column('idEstado', Integer, ForeignKey('estados.id')),
)