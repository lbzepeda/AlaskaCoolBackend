from sqlalchemy import Table, Column, CHAR, NVARCHAR, DECIMAL, DateTime
from sqlalchemy.sql.sqltypes import Integer
from conn.db import meta

det_proforma = Table('DET_PROFORMA', meta,
    Column('Sucursal', CHAR(3), primary_key=True),
    Column('NoFactura', CHAR(8), primary_key=True),
    Column('Serie', CHAR(1), primary_key=True),
    Column('Tipo', CHAR(2), primary_key=True),
    Column('Modo', CHAR(1), primary_key=True),
    Column('FechaFactura', DateTime, primary_key=True),
    Column('Producto', CHAR(20), primary_key=True),
    Column('UMedida', CHAR(2), nullable=False),
    Column('Cantidad', DECIMAL(22, 2), nullable=False),
    Column('Bonificacion', DECIMAL(22, 2), nullable=False),
    Column('Financiamiento', DECIMAL(10, 2), nullable=False),
    Column('Precio', DECIMAL(22, 6), nullable=False),
    Column('Porcen_Descto', DECIMAL(22, 6)),
    Column('Descuento', DECIMAL(22, 6), nullable=False),
    Column('Iva', DECIMAL(22, 6), nullable=False),
    Column('Costo', DECIMAL(22, 6), nullable=False),
    Column('Exonerado', DECIMAL(22, 6), nullable=False),
    Column('Bod_Descargue', CHAR(3), nullable=False),
    Column('CodPrecio', CHAR(2), nullable=False),
    Column('Registro_Usuario', CHAR(50), nullable=False),
    Column('Registro_Maquina', CHAR(50), nullable=False),
    Column('Registro_Fecha', DateTime, nullable=False),
    Column('nombre_producto', NVARCHAR(1000)),
    Column('Tipodesc', CHAR(1), nullable=False),
    Column('orden_manual', Integer, nullable=False),
    Column('cod_combo', NVARCHAR(20), primary_key=True),
    Column('orden1', Integer, nullable=False, primary_key=True),
    Column('Porcentaje_ComisionLista', DECIMAL(5, 2), nullable=False),
    Column('TipoComponente', CHAR(1), nullable=False),
    Column('Gravado', CHAR(1), nullable=False),
    Column('CantidadMovimiento', DECIMAL(22, 6)),
    Column('MedidaCosteo', NVARCHAR(2), nullable=False),
    Column('MedidaMovimiento', NVARCHAR(2), nullable=False),
    Column('Medida_Bonificacion', NVARCHAR(2), nullable=False),
    Column('Bonificacion_movimiento', DECIMAL(22, 2), nullable=False),
    Column('DescuentoFijo', CHAR(1), nullable=False),
    Column('PrioridadDescuento', Integer, nullable=False),
    Column('num_parte', NVARCHAR(500), nullable=False),
    Column('Impuesto1', DECIMAL(22, 6)),
    Column('Impuesto2', DECIMAL(22, 6)),
    Column('Impuesto3', DECIMAL(22, 6)),
    Column('Impuesto4', DECIMAL(22, 6)),
    Column('Impuesto5', DECIMAL(22, 6))
)
