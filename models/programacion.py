from conn.db import meta
from sqlalchemy import ForeignKey
from sqlalchemy import Table, Column, Integer, String, DateTime
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
    Column('UrlGeoLocalizacion', Text),
    Column('direccion', Text, nullable=True),
    Column('observaciones', Text, nullable=True),
    Column('idDepartamento', Integer, ForeignKey('departamentos.id')),
    Column('idEstadoProgramacion', Integer, ForeignKey('estado_programacion.id')),
    Column('idEstado', Integer, ForeignKey('estados.id')),
    Column('CodeGoogleCalendar', Text, nullable=True),
    Column('FechaCreacion', DateTime, nullable=False),
    Column('idTipoProgramacion', Integer, ForeignKey('tipo_programacion.id')),
    Column('nombrecliente', String(500), nullable=True),
    Column('facturascheque', String(500), nullable=True),
)