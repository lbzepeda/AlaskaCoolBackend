from conn.db import meta_sql
from sqlalchemy import PrimaryKeyConstraint, DECIMAL, CHAR, DateTime, Text
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.sql.sqltypes import Integer, String

clientes = Table('clientes', meta_sql,
                 Column('CodCliente', String(20), primary_key=True),
                 Column('Nombres', String(50), nullable=False),
                 Column('Apellidos', String(50), nullable=False),
                 Column('RazonSocial', String(100), nullable=False),
                 Column('Direccion', String(100), nullable=False),
                 Column('Telefonos', String(50), nullable=False),
                 Column('FAX', String(50), nullable=False),
                 Column('Celular', String(50), nullable=False),
                 Column('WebPage', String(100)),
                 Column('Distrito', String(50), nullable=False),
                 Column('Barrio', String(50), nullable=False),
                 Column('CodTipoCliente', String(20), nullable=False),
                 Column('CodVendedor', String(20)),
                 Column('CodSupervisor', String(20), nullable=False)
                 )
