from conn.db import meta
from sqlalchemy import ForeignKey
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.sql.sqltypes import Integer, String

usuarios = Table('usuarios', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('nombre', String(50)),
    Column('correo', String(50)),
    Column('idEstado', Integer, ForeignKey('estados.id'), default=1),
    Column('idTipoUsuario', Integer, ForeignKey('tipo_usuario.id'))
)