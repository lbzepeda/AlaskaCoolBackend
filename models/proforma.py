from sqlalchemy import Table, Column, CHAR, NVARCHAR, DECIMAL, DateTime, Text, Integer
from conn.db import meta

proforma = Table('PROFORMA', meta,
    Column('NoFactura', CHAR(8), primary_key=True),
    Column('Serie', CHAR(1), nullable=False),
    Column('Tipo', CHAR(2), nullable=False),
    Column('Modo', CHAR(1), nullable=False),
    Column('FechaFactura', DateTime, primary_key=True),
    Column('Moneda', CHAR(1), nullable=False),
    Column('Efectivo', DECIMAL(10, 2), nullable=False),
    Column('Tarjeta', DECIMAL(10, 2), nullable=False),
    Column('Cheque', DECIMAL(10, 2), nullable=False),
    Column('RetencionIR', DECIMAL(22, 6)),
    Column('RetencionALMA', DECIMAL(22, 6)),
    Column('SubTotal', DECIMAL(22, 6)),
    Column('Descuento', DECIMAL(22, 6)),
    Column('Iva', DECIMAL(22, 6)),
    Column('MontoExonerado', DECIMAL(10, 2), nullable=False),
    Column('TotalPago', DECIMAL(22, 6)),
    Column('CodListaPrecio', CHAR(2), nullable=False),
    Column('Sucursal', CHAR(3), primary_key=True),
    Column('CodCli', CHAR(6), nullable=False),
    Column('Nombrede', NVARCHAR(200), nullable=False),
    Column('Ruta', CHAR(3), nullable=False),
    Column('Rutero', CHAR(3), nullable=False),
    Column('CentroVenta', CHAR(200), nullable=False),
    Column('Supervisor', CHAR(3), nullable=False),
    Column('Colector', CHAR(3), nullable=False),
    Column('Anulado', CHAR(1), nullable=False),
    Column('valtas', DECIMAL(8, 4), nullable=False),
    Column('Fecha_Vence', DateTime, nullable=False),
    Column('RegistroFecha', DateTime, nullable=False),
    Column('RegistroUsuario', NVARCHAR(50), nullable=False),
    Column('RegistroMaquina', NVARCHAR(50), nullable=False),
    Column('Exonerado', CHAR(1), nullable=False),
    Column('ReferenciaExoneracion', NVARCHAR(50), nullable=False),
    Column('Consignatario', CHAR(1), nullable=False),
    Column('Plazo', DECIMAL(10, 2), nullable=False),
    Column('FormaPago', CHAR(1), nullable=False),
    Column('MontoPrima', DECIMAL(10, 2), nullable=False),
    Column('FechaPagoPrima', DateTime, nullable=False),
    Column('Cuotas', Integer, nullable=False),
    Column('Financiamiento', DECIMAL(10, 2), nullable=False),
    Column('TipoCasa', CHAR(1), nullable=False),
    Column('TiempoResidir', NVARCHAR(30), nullable=False),
    Column('CodTipoCliente', NVARCHAR(3), nullable=False),
    Column('NoIdentificacion', NVARCHAR(40), nullable=False),
    Column('clientecontado', CHAR(200), nullable=False),
    Column('facturado', CHAR(1), nullable=False),
    Column('fechafacturado', DateTime, nullable=False),
    Column('factu', CHAR(8), nullable=False),
    Column('Observaciones', Text, nullable=False),
    Column('MODENA', CHAR(1), nullable=False),
    Column('ref_licitacion', NVARCHAR(20), nullable=False),
    Column('telatencion', NVARCHAR(20), nullable=False),
    Column('atencionde', NVARCHAR(50), nullable=False),
    Column('FechaValida', DateTime, nullable=False),
    Column('CodClienteSucursal', Integer, nullable=False),
    Column('detalle_canje_anticipo', Integer, nullable=False),
    Column('detalle_canje_anticipo_tempo', Integer, nullable=False),
    Column('NombreSubCliente', NVARCHAR(500), nullable=False),
    Column('ClientePadre', NVARCHAR(500), nullable=False),
    Column('Rpt', NVARCHAR(500), nullable=False),
    Column('TiempoEntrega', NVARCHAR(100), nullable=False),
    Column('LugarEntrega', NVARCHAR(100), nullable=False),
    Column('Impuesto1', DECIMAL(22, 6)),
    Column('Impuesto2', DECIMAL(22, 6)),
    Column('Impuesto3', DECIMAL(22, 6)),
    Column('Impuesto4', DECIMAL(22, 6)),
    Column('Impuesto5', DECIMAL(22, 6)),
    Column('LeyendaInformativa', NVARCHAR(500), nullable=False),
)