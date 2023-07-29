from conn.db import meta
from sqlalchemy import DateTime, Time
from sqlalchemy import Table, Column, Integer
from sqlalchemy.sql.sqltypes import Integer

horario_programacion = Table('horario_programacion', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('fechainicio', DateTime, nullable=False),
    Column('fechafin', DateTime, nullable=False),
    Column('horainicio', Time, nullable=False),
    Column('horafin', Time, nullable=False),
)