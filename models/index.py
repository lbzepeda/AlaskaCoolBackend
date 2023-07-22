from importlib.metadata import metadata
from conn.db import engine, meta
from models.usuario import usuarios
from models.factura import facturas
from models.estado import estados

meta.create_all(engine)