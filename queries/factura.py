import typing
import strawberry
from conn.db import conn
from models.index import det_facturas, productos, facturas
from strawberry.types import Info
from typing import Optional
from datetime import datetime
from .detallefactura import *

lstDetFacturas = conn.execute(det_facturas.select()).fetchall()
lstProductos = conn.execute(productos.select()).fetchall()

@strawberry.type
class Factura:
    NoFactura: str
    @strawberry.field
    def det_factura(self, info: Info) -> typing.List[Optional[DetalleFactura]]:  
        detFacturas = [DetalleFactura(**dict(detFactura._mapping)) for detFactura in lstDetFacturas if detFactura.NoFactura == self.NoFactura]
        return detFacturas if detFacturas else []
    Serie: str
    Tipo: str
    Modo: str
    FechaFactura: datetime
    Moneda: str
    Efectivo: float
    Tarjeta: float
    Cheque: float
    RetencionIR: Optional[float] = None
    RetencionALMA: Optional[float] = None
    SubTotal: Optional[float] = None
    Descuento: Optional[float] = None
    Iva: Optional[float] = None
    MontoExonerado: float
    TotalPago: Optional[float] = None
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
    revertida: str
    NumOrden: str
    numprecierre: str
    imprimir: str
    numero: int
    conteo: int
    noapartado: str
    caja: str
    numcierre: Optional[str]
    NoRecerva: str
    Version: str
    NoTransaccionInv: int
    CodClienteSucursal: int
    Cajero: str
    Observacion: str
    VerComoPreventa: str
    TipoServicio: int
    Transporte: float
    Propina: float
    Agente: int
    NombreSubCliente: str
    ClientePadre: str
    NumeroExoneracion: str
    IdentificadorPreventa: int
    ReferenciaPreventa: int
    IdEstado: int
    FechaRetorno: datetime
    MotivoRevertida: str
    HoraRevertida: datetime
    HoraEnviado: datetime
    CantidadCupones: int
    Referencia: str
    NoPedido: str
    EtiquetaInformativa: str
    Longitud: float
    Latitud: float
    IdProgramacion: int
    AplicaGarantia: str
    RegistroFechaApp: datetime
    Impuesto1: Optional[float]
    Impuesto2: Optional[float]
    Impuesto3: Optional[float]
    Impuesto4: Optional[float]
    Impuesto5: Optional[float]
    NumeroTrasladoConsignado: str
    BodDestino: str
    BodDestinoConsignacion: str
    NoConsignacionCLiente: str
    PlanDePago: str
    ROCPRIMA: str
    NoPlanPago: int
    ValorInteres: float
    IdPromocion: str

@strawberry.field
def factura_por_id(NoFactura: str) -> Optional[Factura]:
    return conn.execute(facturas.select().where(facturas.c.NoFactura == NoFactura)).fetchone()

@strawberry.field
def lista_factura(self) -> typing.List[Factura]:
    return conn.execute(facturas.select()).fetchall()

lstFacturaQuery = [factura_por_id, lista_factura]