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

lstProductos = conn.execute(productos.select()).fetchall()
lstProforma = conn.execute(proforma.select()).fetchall()
lstDetProformas = conn.execute(det_proforma.select()).fetchall()
lstUsuarios = conn.execute(usuarios.select()).fetchall()
lstCuadrillas = conn.execute(cuadrillas.select()).fetchall()
lstUsuario_Cuadrilla = conn.execute(usuario_cuadrilla.select()).fetchall()
lstFacturas = conn.execute(facturas.select()).fetchall()
lstDetFacturas = conn.execute(det_facturas.select()).fetchall()
lstHorarioProgramacion = conn.execute(horario_programacion.select()).fetchall()

load_dotenv()
slack_token = os.getenv('SLACK_TOKEN')
ssl._create_default_https_context = ssl._create_unverified_context
client = WebClient(token=slack_token)

def send_message(text: str):
    try:
        response = client.chat_postMessage(
            channel="C05L4FPK7CG",  # Aquí puedes cambiar el ID de tu canal
            text=text)  # Aquí utilizamos la variable text
    except SlackApiError as e:
        print(f"Got an error: {e.response['error']}")
        print(slack_token)

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
class HorarioProgramacion:
    id: int
    fechainicio: datetime
    fechafin: datetime
    horainicio: time
    horafin: time

    @classmethod
    def from_row(cls, row):
        return cls(**row._asdict())

@strawberry.mutation
async def crear_programacion(
    self, 
    codservicio: str, 
    idUsuarioCreacion: int, 
    UrlGeoLocalizacion: str, 
    info: Info,
    codcliente: Optional[str] = None, 
    codfactura: Optional[str] = None, 
    codproforma: Optional[str] = None,
    idCuadrilla: Optional[int] = None, 
    idHorarioProgramacion: Optional[int] = None,
    direccion: Optional[str] = None,
    observaciones: Optional[str] = None,
    IdDepartamento: Optional[int] = None,) -> int:
    
    data_programacion = {
        "codservicio": codservicio,
        "idUsuarioCreacion": idUsuarioCreacion,
        "UrlGeoLocalizacion": UrlGeoLocalizacion,
        "codcliente": codcliente,
        "codfactura": codfactura,
        "codproforma": codproforma,
        "idCuadrilla": idCuadrilla,
        "idHorarioProgramacion": idHorarioProgramacion,
        "direccion": direccion,
        "observaciones": observaciones,
        "idDepartamento": IdDepartamento,
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
    #send_message(text)
    conn.commit()
    return int(result.inserted_primary_key[0])

@strawberry.mutation
def actualizar_programacion(self, id: int, 
    codservicio: str, 
    idUsuarioCreacion: int, 
    UrlGeoLocalizacion: str, 
    info: Info,
    codcliente: Optional[str] = None, 
    codfactura: Optional[str] = None, 
    codproforma: Optional[str] = None,
    idCuadrilla: Optional[int] = None, 
    idHorarioProgramacion: Optional[int] = None,
    direccion: Optional[str] = None,
    observaciones: Optional[str] = None,
    IdDepartamento: Optional[str] = None) -> str:
    result = conn.execute(programacion.update().where(programacion.c.id == id), {
        "codservicio": codservicio,
        "idUsuarioCreacion": idUsuarioCreacion,
        "UrlGeoLocalizacion": UrlGeoLocalizacion,
        "codcliente": codcliente,
        "codfactura": codfactura,
        "codproforma": codproforma,
        "idCuadrilla": idCuadrilla,
        "idHorarioProgramacion": idHorarioProgramacion,
        "direccion": direccion,
        "observaciones": observaciones,
        "idDepartamento": IdDepartamento,
    })
    print(result. returns_rows)
    conn.commit()
    return str(result.rowcount) + " Row(s) updated"

lstProgramacionMutation = [crear_programacion, actualizar_programacion]