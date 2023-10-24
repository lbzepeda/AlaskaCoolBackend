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
from models.programacion import programacion
from models.departamentos import departamentos
from models.estadoprogramacion import estado_programacion
from models.tipoarchivo import tipo_archivo
from models.archivoprogramacion import archivo_programacion
from models.tipoprogramacion import tipo_programacion
from models.bancos import bancos
from models.clientes import clientes
from models.requisa import requisa
from models.detallerequisa import detalle_requisa
from models.genero import genero
from models.cargo import cargo
from models.moneda import moneda
from models.colaboradores import colaboradores
from models.archivos import archivos
from models.contratacionescolaboradores import contratacion_colaboradores
from models.esquemapago import esquema_pago
from models.tipopago import tipo_pago
from models.fechapago import fecha_pago

meta.create_all(engine)