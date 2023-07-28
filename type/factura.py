import typing
import strawberry
from conn.db import conn
from models.index import det_facturas, productos, facturas
from strawberry.types import Info
from typing import Optional
from datetime import datetime
from decimal import Decimal

lstDetFacturas = conn.execute(det_facturas.select()).fetchall()
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
class DetalleFactura:
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


@strawberry.type
class Query:
    @strawberry.field
    def factura(NoFactura: str) -> Optional[Factura]:
        return conn.execute(facturas.select().where(facturas.c.NoFactura == NoFactura)).fetchone()

    @strawberry.field
    def facturas(self) -> typing.List[Factura]:
        return conn.execute(facturas.select()).fetchall()
