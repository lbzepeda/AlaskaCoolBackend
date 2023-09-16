from conn.db import meta
from sqlalchemy import ForeignKey
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.sql.sqltypes import Integer, String, Text

archivo_programacion = Table('archivo_programacion', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('PathArchivo', Text),
    Column('idTipoArchivo', Integer, ForeignKey('tipo_archivo.id')),
    # Column('idProgramacion', Integer, ForeignKey('programacion.id')),
    Column('codProgramacion', String(50), nullable=True),
    Column('NombreArchivo', String(1000))
)