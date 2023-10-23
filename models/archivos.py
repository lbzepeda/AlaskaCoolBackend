from conn.db import meta
from sqlalchemy import ForeignKey
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.sql.sqltypes import Integer, String, Text

archivos = Table('archivos', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('PathArchivo', Text),
    Column('idTipoArchivo', Integer, ForeignKey('tipo_archivo.id')),
    Column('NombreArchivo', String(1000)),
    Column('idContratacionesColaboradores',  Integer, ForeignKey('contratacion_colaboradores.id')),
)