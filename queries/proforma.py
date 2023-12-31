import typing
import strawberry
from conn.db import conn_sql
from models.index import proforma, det_proforma
from strawberry.types import Info
from typing import Optional
from datetime import datetime
from .detalleproforma import *

@strawberry.type
class Proforma:
    NoFactura: str
    @strawberry.field
    def det_proforma(self, info: Info) -> typing.List[Optional[DetalleProforma]]:
        current_det_proformas = conn_sql.execute(det_proforma.select()).fetchall()

        matched_proformas = [
            DetalleProforma(**dict(det._mapping))
            for det in current_det_proformas 
            if det.NoFactura == self.NoFactura
        ]
        return matched_proformas or []
    Serie: str
    Tipo: str
    Modo: str
    FechaFactura: datetime
    Moneda: str
    Efectivo: float
    Tarjeta: float
    Cheque: float
    RetencionIR: Optional[float]
    RetencionALMA: Optional[float]
    SubTotal: Optional[float]
    Descuento: Optional[float]
    Iva: Optional[float]
    MontoExonerado: float
    TotalPago: Optional[float]
    CodListaPrecio: str
    Sucursal: str
    CodCli: str
    Nombrede: str
    Ruta: str
    Rutero: str
    CentroVenta: str
    Supervisor: str
    Colector: str
    Anulado: str
    valtas: float
    Fecha_Vence: datetime
    RegistroFecha: datetime
    RegistroUsuario: str
    RegistroMaquina: str
    Exonerado: str
    ReferenciaExoneracion: str
    Consignatario: str
    Plazo: float
    FormaPago: str
    MontoPrima: float
    FechaPagoPrima: datetime
    Cuotas: int
    Financiamiento: float
    TipoCasa: str
    TiempoResidir: str
    CodTipoCliente: str
    NoIdentificacion: str
    clientecontado: str
    facturado: str
    fechafacturado: datetime
    factu: str
    Observaciones: str
    MODENA: str
    ref_licitacion: str
    telatencion: str
    atencionde: str
    FechaValida: datetime
    CodClienteSucursal: int
    detalle_canje_anticipo: int
    detalle_canje_anticipo_tempo: int
    NombreSubCliente: str
    ClientePadre: str
    Rpt: str
    TiempoEntrega: str
    LugarEntrega: str
    Impuesto1: Optional[float]
    Impuesto2: Optional[float]
    Impuesto3: Optional[float]
    Impuesto4: Optional[float]
    Impuesto5: Optional[float]
    LeyendaInformativa: str

@strawberry.field
def proforma_por_id(NoFactura: str) -> Optional[Proforma]:
    result = conn_sql.execute(proforma.select().where(proforma.c.NoFactura == NoFactura)).fetchone()
    return result

@strawberry.field
def lista_proforma(self) -> typing.List[Proforma]:
    result = conn_sql.execute(proforma.select()).fetchall()
    return result

lstProformaQuery = [proforma_por_id, lista_proforma]