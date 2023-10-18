from sqlalchemy import Table, Column, String, NVARCHAR, DECIMAL, DateTime
from sqlalchemy.sql.sqltypes import Integer, Text
from sqlalchemy import ForeignKey
from conn.db import meta

requisa = Table('requisa', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('FechaCreacion', DateTime, nullable=False),
    Column('idUsuarioCreacion', Integer, ForeignKey('usuarios.id')),
    Column('idEstado', Integer, ForeignKey('estados.id')),
    Column('observaciones', Text, nullable=True),
    Column('codfactura', String(50), nullable=True)
)