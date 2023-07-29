from importlib.metadata import metadata
from conn.db import engine, meta
from models.usuario import usuarios
from models.factura import facturas
from models.estado import estados
from models.tipousuario import tipo_usuario
from models.cuadrilla import cuadrillas
from models.usuariocuadrilla import usuario_cuadrilla
from models.detallefatura import det_facturas
from models.producto import productos
from models.detalleproforma import det_proforma
from models.proforma import proforma
from models.horarioprogramacion import horario_programacion

meta.create_all(engine)