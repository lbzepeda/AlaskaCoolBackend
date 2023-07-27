from importlib.metadata import metadata
from conn.db import engine, meta
from models.usuario import usuarios
from models.factura import facturas
from models.estado import estados
from models.tipousuario import tipo_usuario
from models.cuadrilla import cuadrillas

meta.create_all(engine)