from conn.db import meta
from sqlalchemy import ForeignKey
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.sql.sqltypes import Integer, String, Text

programacion = Table('programacion', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('codservicio', String(50)),
    Column('codcliente', String(50), nullable=True),
    Column('codfactura', String(50), nullable=True),
    Column('codproforma', String(50), nullable=True),
    Column('idUsuarioCreacion', Integer, ForeignKey('usuarios.id')),
    Column('idCuadrilla', Integer, ForeignKey('cuadrilla.id'), nullable=True),
    Column('idHorarioProgramacion', Integer, ForeignKey('horario_programacion.id'), nullable=True),
    Column('UrlGeoLocalizacion', Text)
)