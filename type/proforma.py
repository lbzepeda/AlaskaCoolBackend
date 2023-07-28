import typing
import strawberry
from conn.db import conn
from models.index import proforma, det_proforma, productos
from strawberry.types import Info
from typing import Optional
from datetime import datetime
from decimal import Decimal

lstDetProformas = conn.execute(det_proforma.select()).fetchall()
lstProductos = conn.execute(productos.select()).fetchall()

@strawberry.type
class Productos:
    CodProducto: str
    descripcion: str
    CodProveedor: int
    Referencia: Optional[str] = None
    Cod_Linea: str
    CodUm: str
    CostoFOB: float
    Costo: float
    Precio1: float
    Precio2: float
    Precio3: float
    Precio4: float
    Existencia: float
    NoExistencia: str
    Activo: str
    InventMinimo: float
    CuentaProducto: str
    Gravable: str
    PorcComision: float
    Consignacion: str
    Moneda: str
    CodDescuento: str
    CodTipoProducto: str
    CodUbicacion: str
    DiasDevolucion: float
    PrecioXDefecto: str
    Referencia1: str
    Referencia2: Optional[str] = None
    Referencia3: str
    Uso: str
    Promocion: Optional[float] = None
    Promocion2: Optional[float] = None
    CostoMP: Optional[float] = None
    ParaVenta: str
    CtaVenta: str
    Ctainventario: str
    CtaCosto: str
    codigogrupo: str
    codigomarca: str
    ICS: str
    MaquinaRegistro: str
    UsuarioRegistro: str
    FechaRegistro: datetime
    controlaexistencia: str
    codBarra: Optional[str] = None
    codSAP: str
    modelo: str
    eficiencia: str
    capacidad: str
    watt: str
    tecnologia: str
    stockMIN: int
    stockMAX: int
    num_parte: str
    codigogarantia: str
    combo: str
    DIBUJO: str
    presentacion: str
    Version: str
    CodigoMoneda: int
    EsServicio: str
    DescripcionEditable: str
    TipoCombo: str
    ValidaCantida: str
    MedidaCompra: str
    volumen: float
    alto: float
    ancho: float
    longitud: float
    peso: float
    Controlado: str
    MsjControlado: str
    Descripcion2: str
    IdProducto: int
    SegundoNombre: str
    PermiteCero: str
    PermiteDecuento: str
    MontoDescuento: float
    AplicaUltimoDiaDeVenta: str
    UltimoDiaDeVenta: Optional[datetime] = None
    Color: str
    ComboRespetaBodegAsociada: str
    PrecioLibre: str
    LibreDesde: float
    LibreHasta: float
    AplicaWeb: str
    AplicaMovil: str
    departamento: int
    Bonificacion: str
    InsumoProduccion: str
    ProductoTerminado: str
    Mensaje: str
    FechaCaducidadMensaje: Optional[datetime] = None
    ColorMensaje: str
    UnicoEnFactura: str
    PrimerDiaDeVenta: Optional[datetime] = None
    VisibleEnServicios: str
    AplicaCalendario: str
    SoyPrimeraEleccion: str
    TengoPrimeraEleccion: str
    AplicaLote: str
    AplicaVencimiento: str
    DiasRetiro: int
    OrigenCrecion: str
    IdColor: int
    IdTalla: int
    Importado: str
    AlimentoBebida: str
    CodificacionMsv: str
    idRubro: int
    IdKilate: int
    IdestadoPrenda: int
    Externo: str
    CertificadoValor: str
    TipoInventario: int
    UltimoDiaDeCompra: Optional[datetime] = None
    idSeccion: int
    idGiroNegocio: int
    ConsignacionCliente: str
    ConsignacionProveedor: str
    NoFactura: str
    Poliza: str
    CodCliente: str
    Impuesto1: float
    Impuesto2: float
    Impuesto3: float
    Impuesto4: float
    Impuesto5: float
    ComentarioVendedor: str
    CodBarras2: str
    EsPizza: str
    TiempoPreparacion: str
    Largo: float
    Profundidad: float
    PesoReal: float
    PesoVolumetrico: float
    codigotamano: int
    AreaImpresion: str
    PermiteDevolucionFactura: str
    CodigoAlterno: str
    DerechoAutor: str

@strawberry.type
class DetalleProforma:
    Sucursal: str
    NoFactura: str
    Serie: str
    Tipo: str
    Modo: str
    FechaFactura: datetime
    Producto: str
    @strawberry.field
    def producto(self, info: Info) -> typing.List[Optional[Productos]]:  
        productos = [Productos(**dict(producto._mapping)) for producto in lstProductos if producto.CodProducto == self.Producto]
        return productos if productos else []
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

@strawberry.type
class Proforma:
    NoFactura: str
    @strawberry.field
    def det_proforma(self, info: Info) -> typing.List[Optional[DetalleProforma]]:  
        detFacturas = [DetalleProforma(**dict(detFactura._mapping)) for detFactura in lstDetProformas if detFactura.NoFactura == self.NoFactura]
        return detFacturas if detFacturas else []
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

@strawberry.type
class Query:
    @strawberry.field
    def proforma(NoFactura: str) -> Optional[Proforma]:
        return conn.execute(proforma.select().where(proforma.c.NoFactura == NoFactura)).fetchone()

    @strawberry.field
    def proformas(self) -> typing.List[Proforma]:
        return conn.execute(proforma.select()).fetchall()
