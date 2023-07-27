from conn.db import meta
from sqlalchemy import ForeignKey
from sqlalchemy import Table, Column, Integer
from sqlalchemy.sql.sqltypes import Integer

usuario_cuadrilla = Table('usuario_cuadrilla', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('idUsuario', Integer, ForeignKey('usuarios.id')),
    Column('idCuadrilla', Integer, ForeignKey('cuadrilla.id'))
)