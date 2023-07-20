from importlib.metadata import metadata
from conn.db import engine, meta
from models.user import users
from models.factura import facturas

meta.create_all(engine)