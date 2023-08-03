import typing
import strawberry
from conn.db import conn
from models.index import det_facturas
from typing import Optional
from datetime import datetime
from decimal import Decimal

@strawberry.type
class DetalleFactura:
    Sucursal: str
    NoFactura: str
    Serie: str
    Tipo: str
    Modo: str
    FechaFactura: datetime
    Producto: str
    UMedida: str
    Cantidad: Optional[Decimal]
    Bonificacion: Decimal
    Financiamiento: Decimal
    Precio: Optional[Decimal]
    Porcen_Descto: Optional[Decimal]
    Descuento: Optional[Decimal]
    Iva: Optional[Decimal]
    Costo: Decimal
    Exonerado: Optional[Decimal]
    Bod_Descargue: str
    CodPrecio: str
    Registro_Usuario: Optional[str]
    Registro_Maquina: Optional[str]
    Registro_Fecha: Optional[datetime]
    nombre_producto: Optional[str]
    Tipodesc: Optional[str]
    tipofac: str
    Numero: int
    valor: Optional[Decimal]
    cod_combo: str
    orden: int
    indice: int
    Porcentaje_ComisionLista: Decimal
    TipoComponente: str
    Gravado: str
    MedidaCosteo: str
    MedidaMovimiento: str
    CantidadMovimiento: Optional[Decimal]
    Medida_Bonificacion: str
    Bonificacion_Movimiento: Optional[Decimal]
    saldo: Decimal
    PrecioDeLista: Decimal
    DescuentoFijo: str
    PrioridadDescuento: int
    TipoServicio: int
    Cupones: int
    Lote: str
    Vencimiento: datetime
    Receta: str
    Ruta: int
    IdProgramacion: int
    RegistroFechaApp: datetime
    num_parte: str
    OrdenServicio: str
    CentroCosto2: int
    CentroCosto3: int
    Impuesto1: Optional[Decimal]
    Impuesto2: Optional[Decimal]
    Impuesto3: Optional[Decimal]
    Impuesto4: Optional[Decimal]
    Impuesto5: Optional[Decimal]
    ProductoConsignado: str
    NumeroTrasladoConsignado: Optional[str]

@strawberry.field
def detalle_factura_por_id(NoFactura: str) -> typing.List[DetalleFactura]:
    return conn.execute(det_facturas.select().where(det_facturas.c.NoFactura == NoFactura)).fetchall()
@strawberry.field
def detalles_factura(self) -> typing.List[DetalleFactura]:
    return conn.execute(det_facturas.select()).fetchall()

lstDetalleFacturaQuery = [detalle_factura_por_id, detalles_factura]