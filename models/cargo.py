from conn.db import meta
from sqlalchemy import Table, Column, Integer, String, Boolean, Float, DateTime
from datetime import datetime
from sqlalchemy import ForeignKey

cargo = Table('cargo', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('nombre', String(50)),
    Column('descripcion', String(50)),
    Column('responsabilidades', String(500)),
    Column('idEstado', Integer, ForeignKey('estados.id')),
)