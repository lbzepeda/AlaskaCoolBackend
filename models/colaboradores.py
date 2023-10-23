from conn.db import meta
from sqlalchemy import ForeignKey
from sqlalchemy import Table, Column, Integer, String, DateTime
from sqlalchemy.sql.sqltypes import Integer, String, Text

colaboradores = Table('colaboradores', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('PrimerNombre', String(50)),
    Column('SegundoNombre', String(50)),
    Column('PrimerApellido', String(50)),
    Column('SegundoApellido', String(50)),
    Column('CorreoPersonal', String(50)),
    Column('CorreoInstitucional', String(50)),
    Column('FechaNacimiento', DateTime, nullable=False),
    Column('idGenero', Integer, ForeignKey('genero.id')),
    Column('idEstado', Integer, ForeignKey('estados.id')),
)