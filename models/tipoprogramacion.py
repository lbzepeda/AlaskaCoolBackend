from conn.db import meta
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.sql.sqltypes import Integer, String

tipo_programacion = Table('tipo_programacion', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('nombre', String(50)),
    Column('descripcion', String(50)),
)