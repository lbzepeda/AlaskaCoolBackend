from sqlalchemy import Table, Column, String, NVARCHAR, DECIMAL, DateTime
from sqlalchemy.sql.sqltypes import Integer, Text
from sqlalchemy import ForeignKey
from conn.db import meta

detalle_requisa = Table('detalle_requisa', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('idRequisa', Integer, ForeignKey('requisa.id')),
    Column('CodProducto', Text, nullable=True),
    Column('cantidad', String(50), nullable=True),
    Column('idEstado', Integer, ForeignKey('estados.id')),
    Column('NoSerie', Text, nullable=True),
)