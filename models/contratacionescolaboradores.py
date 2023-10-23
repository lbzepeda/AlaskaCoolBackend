from conn.db import meta
from sqlalchemy import ForeignKey
from sqlalchemy import Table, Column, Integer, String, DateTime
from sqlalchemy.sql.sqltypes import Integer, String, Text

contratacion_colaboradores = Table('contratacion_colaboradores', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('SalarioBase', String(50)),
    Column('SalarioMoneda', Integer, ForeignKey('moneda.id')),
    Column('FechaInicio', DateTime, nullable=False),
    Column('FechaFin', DateTime),
    Column('idCargo', Integer, ForeignKey('cargo.id')),
    Column('idColaborador', Integer, ForeignKey('colaboradores.id')),
    Column('idEstado', Integer, ForeignKey('estados.id')),
)