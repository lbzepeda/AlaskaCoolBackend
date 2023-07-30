import typing
import strawberry
from conn.db import conn
from models.index import programacion, productos, proforma, det_proforma, usuarios, cuadrillas, usuario_cuadrilla, facturas, det_facturas, horario_programacion
from strawberry.types import Info
from datetime import datetime
from typing import Optional
from decimal import Decimal
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import ssl
from dotenv import load_dotenv
from datetime import time

#load_dotenv()
slack_token = os.getenv('SLACK_TOKEN')
ssl._create_default_https_context = ssl._create_unverified_context
client = WebClient(token=slack_token)

lstProductos = conn.execute(productos.select()).fetchall()
lstProforma = conn.execute(proforma.select()).fetchall()
lstDetProformas = conn.execute(det_proforma.select()).fetchall()
lstUsuarios = conn.execute(usuarios.select()).fetchall()
lstCuadrillas = conn.execute(cuadrillas.select()).fetchall()
lstUsuario_Cuadrilla = conn.execute(usuario_cuadrilla.select()).fetchall()
lstFacturas = conn.execute(facturas.select()).fetchall()
lstDetFacturas = conn.execute(det_facturas.select()).fetchall()

def send_message(text: str):
    try:
        response = client.chat_postMessage(
            channel="C05L4FPK7CG",  # Aquí puedes cambiar el ID de tu canal
            text=text)  # Aquí utilizamos la variable text
    except SlackApiError as e:
        print(f"Got an error: {e.response['error']}")
        print(slack_token)

@strawberry.type
class HorarioProgramacion:
    id: int
    fechainicio: datetime
    fechafin: datetime
    horainicio: time
    horafin: time

    @classmethod
    def from_row(cls, row):
        return cls(**row._asdict())

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
    Moneda: Optional[str] = None
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

    @classmethod
    def from_row(cls, row):
        return cls(**row._asdict())

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
class Usuario:
    id: int
    nombre: str
    correo: str
    idEstado: int
    idTipoUsuario: int

    @classmethod
    def from_row(cls, row):
        return cls(**row._asdict())

@strawberry.type
class Cuadrilla:
    id: int
    nombre: str
    descripcion: str

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
class UsuarioCuadrilla:
    id: int
    idUsuario: int
    @strawberry.field
    def usuarios(self, info: Info) -> typing.List[Optional[Usuario]]:
        usuarios_con_id = [usuario for usuario in lstUsuarios if usuario.id == self.idUsuario]
        return [Usuario(**dict(usuario._mapping)) for usuario in usuarios_con_id]
    idCuadrilla: int
    @strawberry.field
    def cuadrilla(self, info: Info) -> Optional[Cuadrilla]:  
        cuadrilla = next((cuadrillas for cuadrillas in lstCuadrillas if cuadrillas.id == self.idCuadrilla), None)
        if cuadrilla:
            return Cuadrilla(**dict(cuadrilla._mapping))
        else:
            return None

@strawberry.type
class Programacion:
    id: int
    codservicio: str
    @strawberry.field
    def servicio(self, info: Info) -> typing.List[Optional[Productos]]:  
        productos = [Productos(**dict(producto._mapping)) for producto in lstProductos if producto.CodProducto == self.codservicio]
        return productos if productos else []
    codcliente: Optional[str] = None
    codfactura: Optional[str] = None
    @strawberry.field
    def factura(self, info: Info) -> Optional[Factura]:  
        facturas = [Factura(**dict(factura._mapping)) for factura in lstFacturas if factura and factura.NoFactura == self.codfactura]
        return facturas[0] if facturas else None
    codproforma: Optional[str] = None
    @strawberry.field
    def proforma(self, info: Info) -> Optional[Proforma]:  
        proformas = [Proforma(**dict(proforma._mapping)) for proforma in lstProforma if proforma and proforma.NoFactura == self.codproforma]
        return proformas[0] if proformas else None
    idUsuarioCreacion: int
    idCuadrilla: Optional[int] = None
    @strawberry.field
    def cuadrilla(self, info: Info) -> typing.List[Optional[UsuarioCuadrilla]]:  
        usuariocuadrilla = [UsuarioCuadrilla(**dict(usuario_cuadrilla._mapping)) for usuario_cuadrilla in lstUsuario_Cuadrilla if usuario_cuadrilla.idCuadrilla == self.idCuadrilla]
        return usuariocuadrilla if usuariocuadrilla else []
    idHorarioProgramacion: Optional[int] = None
    UrlGeoLocalizacion: str

    @classmethod
    def from_row(cls, row):
        return cls(**row)


@strawberry.type
class Query:
    @strawberry.field
    def programacion(id: int) -> Optional[Programacion]:
        return conn.execute(programacion.select().where(programacion.c.id == id)).fetchone()

    @strawberry.field
    def programaciones(self) -> typing.List[Programacion]:
        return conn.execute(programacion.select()).fetchall()


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_programacion(
        self, 
        codservicio: str, 
        idUsuarioCreacion: int, 
        UrlGeoLocalizacion: str, 
        info: Info,
        codcliente: Optional[str] = None, 
        codfactura: Optional[str] = None, 
        codproforma: Optional[str] = None,
        idCuadrilla: Optional[int] = None, 
        idHorarioProgramacion: Optional[int] = None) -> int:
        
        data_programacion = {
            "codservicio": codservicio,
            "idUsuarioCreacion": idUsuarioCreacion,
            "UrlGeoLocalizacion": UrlGeoLocalizacion,
            "codcliente": codcliente,
            "codfactura": codfactura,
            "codproforma": codproforma,
            "idCuadrilla": idCuadrilla,
            "idHorarioProgramacion": idHorarioProgramacion,
        }
        result = conn.execute(programacion.insert(), data_programacion)
        
        usuario_row = conn.execute(usuarios.select().where(usuarios.c.id == idUsuarioCreacion)).fetchone()
        servicio_row = conn.execute(productos.select().where(productos.c.CodProducto == codservicio)).fetchone()
        horario_row = conn.execute(horario_programacion.select().where(horario_programacion.c.id == idHorarioProgramacion)).fetchone()

        servicio = Productos.from_row(servicio_row)
        usuario = Usuario.from_row(usuario_row)
        horario = HorarioProgramacion.from_row(horario_row)

        text = f"El usuario *{usuario.nombre}* creo una nueva programación para el servicio *{servicio.descripcion}*, para el dia {horario.fechainicio.strftime('%Y-%m-%d')} a las {horario.horainicio.strftime('%H:%M')}."

        print(f"texto {text}")
        send_message(text)
        conn.commit()
        return int(result.inserted_primary_key[0])

    @strawberry.mutation
    def update_usuario(self, id: int, 
        codservicio: str, 
        idUsuarioCreacion: int, 
        UrlGeoLocalizacion: str, 
        info: Info,
        codcliente: Optional[str] = None, 
        codfactura: Optional[str] = None, 
        codproforma: Optional[str] = None,
        idCuadrilla: Optional[int] = None, 
        idHorarioProgramacion: Optional[int] = None) -> str:
        result = conn.execute(programacion.update().where(programacion.c.id == id), {
            "codservicio": codservicio,
            "idUsuarioCreacion": idUsuarioCreacion,
            "UrlGeoLocalizacion": UrlGeoLocalizacion,
            "codcliente": codcliente,
            "codfactura": codfactura,
            "codproforma": codproforma,
            "idCuadrilla": idCuadrilla,
            "idHorarioProgramacion": idHorarioProgramacion,
        })
        print(result. returns_rows)
        conn.commit()
        return str(result.rowcount) + " Row(s) updated"
