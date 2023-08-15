import typing
import strawberry
from conn.db import conn
from models.index import det_proforma, productos
from typing import Optional
from datetime import datetime
from .productos import Productos
from strawberry.types import Info

@strawberry.type
class DetalleProforma:
    Sucursal: str
    NoFactura: str
    Serie: str
    Tipo: str
    Modo: str
    FechaFactura: datetime
    Producto: str
    def producto(self, info: Info) -> Productos:
        lstProductos = conn.execute(productos.select().where(productos.c.CodProducto == self.Producto)).fetchall()
        matched_producto = next((Productos(**dict(producto._mapping)) for producto in lstProductos), None)
        return matched_producto
    UMedida: str
    Cantidad: float
    Bonificacion: float
    Financiamiento: float
    Precio: float
    Porcen_Descto: Optional[float] = None
    Descuento: float
    Iva: float
    Costo: float
    Exonerado: float
    Bod_Descargue: str
    CodPrecio: str
    Registro_Usuario: str
    Registro_Maquina: str
    Registro_Fecha: datetime
    nombre_producto: Optional[str] = None
    Tipodesc: str
    orden_manual: int
    cod_combo: str
    orden1: int
    Porcentaje_ComisionLista: float
    TipoComponente: str
    Gravado: str
    CantidadMovimiento: Optional[float] = None
    MedidaCosteo: str
    MedidaMovimiento: str
    Medida_Bonificacion: str
    Bonificacion_movimiento: float
    DescuentoFijo: str
    PrioridadDescuento: int
    num_parte: str
    Impuesto1: Optional[float] = None
    Impuesto2: Optional[float] = None
    Impuesto3: Optional[float] = None
    Impuesto4: Optional[float] = None
    Impuesto5: Optional[float] = None

@strawberry.field
def detalle_proforma_por_id(NoFactura: str) -> typing.List[DetalleProforma]:
    result = conn.execute(det_proforma.select().where(det_proforma.c.NoFactura == NoFactura)).fetchall()
    conn.commit()
    return result
@strawberry.field
def detalles_proforma(self) -> typing.List[DetalleProforma]:
    result = conn.execute(det_proforma.select()).fetchall()
    conn.commit()
    return result

lstDetalleProformaQuery = [detalle_proforma_por_id, detalles_proforma]