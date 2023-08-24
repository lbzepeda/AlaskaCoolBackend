import strawberry
from conn.db import conn
from models.index import programacion, productos, proforma, det_proforma, usuarios, cuadrillas, usuario_cuadrilla, facturas, det_facturas, horario_programacion
from strawberry.types import Info
from datetime import datetime
from typing import Optional
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import ssl
from dotenv import load_dotenv
from datetime import time
from datetime import datetime
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from datetime import timedelta
from enum import Enum
from json import dumps
from httplib2 import Http


class TipoUsuario(Enum):
    Tecnico = 1
    Ayudante = 2
    GerenteDeVenta = 3
    Vendedor = 4
    SupervisorTecnico = 5


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
# slack_token = os.getenv('SLACK_TOKEN')
# client = WebClient(token=slack_token)
ssl._create_default_https_context = ssl._create_unverified_context
webhook_programing = os.getenv('WEBHOOK_PROGRAMACION_URL')


def create_google_calendar_event(horario_row, servicio, facturaobj, proformaobj, direccion, UrlGeoLocalizacion, observaciones, referencia):
    # Carga las credenciales de la cuenta de servicio
    creds = Credentials.from_service_account_file('alaskacool-ee34eec8f111.json',
                                                  scopes=['https://www.googleapis.com/auth/calendar'])

    # Usa las credenciales para acceder al servicio de Google Calendar
    service = build('calendar', 'v3', credentials=creds)

    cliente = facturaobj.Nombrede if facturaobj else (
        proformaobj.Nombrede if proformaobj else "")

    start_datetime = horario_row.fechainicio.replace(
        hour=horario_row.horainicio.hour, minute=horario_row.horainicio.minute, second=horario_row.horainicio.second)
    end_datetime = horario_row.fechafin.replace(
        hour=horario_row.horafin.hour, minute=horario_row.horafin.minute, second=horario_row.horafin.second)

    direccion = direccion if direccion else "N/A"
    UrlGeoLocalizacion = UrlGeoLocalizacion if UrlGeoLocalizacion else "N/A"
    observaciones = observaciones if observaciones else "N/A"

    # Evento a crear
    event = {
        # Puedes personalizar este texto
        'summary': cliente + ' - ' + servicio.descripcion + ' - Referencia: ' + referencia,
        # Puedes personalizar este texto
        'description':  f'Direccion: {direccion}\nLocalización: {UrlGeoLocalizacion}\nObservaciones: {observaciones}',
        'start': {
            'dateTime': start_datetime.strftime('%Y-%m-%dT%H:%M:%S'),
            'timeZone': 'America/Managua',
        },
        'end': {
            'dateTime': end_datetime.strftime('%Y-%m-%dT%H:%M:%S'),
            'timeZone': 'America/Managua',
        },
    }

    calendar_id = 'bdb1c1dd54cb4991313cbcfda21f549b35e0d40f0103f06812e8dc86f5b20a91@group.calendar.google.com'

    # Usa el método insert del servicio de calendar para crear el evento
    created_event = service.events().insert(
        calendarId=calendar_id, body=event).execute()
    print(f"Evento calendario: {created_event['id']}")
    return created_event['id']  # Retorna el ID del evento creado


def delete_google_calendar_event(event_id):
    # Carga las credenciales de la cuenta de servicio
    creds = Credentials.from_service_account_file('alaskacool-ee34eec8f111.json',
                                                  scopes=['https://www.googleapis.com/auth/calendar'])

    # Usa las credenciales para acceder al servicio de Google Calendar
    service = build('calendar', 'v3', credentials=creds)

    calendar_id = 'bdb1c1dd54cb4991313cbcfda21f549b35e0d40f0103f06812e8dc86f5b20a91@group.calendar.google.com'

    # Eliminar el evento
    service.events().delete(calendarId=calendar_id, eventId=event_id).execute()


def send_message(text: str):
    def main():
        url = webhook_programing
        app_message = {
            'text': str
        }
        message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
        http_obj = Http()
        response = http_obj.request(
            uri=url,
            method='POST',
            headers=message_headers,
            body=dumps(app_message),
        )
        print(response)
    # try:
    #     response = client.chat_postMessage(
    #         channel="C05L4FPK7CG",  # Aquí puedes cambiar el ID de tu canal
    #         text=text)  # Aquí utilizamos la variable text
    # except SlackApiError as e:
    #     print(f"Got an error: {e.response['error']}")
    #     print(slack_token)


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
        idUsuarioCreacion: Optional[int],
        UrlGeoLocalizacion: str,
        info: Info,
        codcliente: Optional[str] = None,
        codfactura: Optional[str] = None,
        codproforma: Optional[str] = None,
        direccion: Optional[str] = None,
        observaciones: Optional[str] = None,
        idDepartamento: Optional[int] = None,
        idHorarioProgramacion: Optional[int] = None,
        idEstadoProgramacion: Optional[int] = None) -> int:

    data_programacion = {
        "codservicio": codservicio,
        "idUsuarioCreacion": idUsuarioCreacion,
        "UrlGeoLocalizacion": UrlGeoLocalizacion,
        "codcliente": codcliente,
        "codfactura": codfactura,
        "codproforma": codproforma,
        "direccion": direccion,
        "observaciones": observaciones,
        "idDepartamento": idDepartamento,
        "idEstadoProgramacion": idEstadoProgramacion,
        "idHorarioProgramacion": idHorarioProgramacion
    }
    result = conn.execute(programacion.insert(), data_programacion)

    usuario_row = conn.execute(usuarios.select().where(
        usuarios.c.id == idUsuarioCreacion)).fetchone()
    servicio_row = conn.execute(productos.select().where(
        productos.c.CodProducto == codservicio)).fetchone()

    servicio = Productos.from_row(servicio_row)
    usuario = Usuario.from_row(usuario_row)

    ref_value = codfactura if codfactura else codproforma
    id_value = result.inserted_primary_key[0]
    text = f"El usuario *{usuario.nombre}* creó una nueva programación para el servicio *{servicio.descripcion}*, Ref: *{ref_value}*. Registro pendiente de asignación de horario y cuadrilla. URL: https://alaska-cool-programacion.vercel.app/registerprograming/{id_value}"

    print(f"texto {text}")
    if idUsuarioCreacion != 1:
        send_message(text)
    conn.commit()
    return int(result.inserted_primary_key[0])


def get_usuario(idUsuarioActualizador):
    usuario_row = conn.execute(usuarios.select().where(
        usuarios.c.id == idUsuarioActualizador)).fetchone()
    return Usuario.from_row(usuario_row)


def get_servicio(codservicio):
    servicio_row = conn.execute(productos.select().where(
        productos.c.CodProducto == codservicio)).fetchone()
    return Productos.from_row(servicio_row)


def get_referencia(codfactura, codproforma):
    return codfactura if codfactura else codproforma


def get_proforma_or_factura(referencia):
    proformaobj = conn.execute(proforma.select().where(
        proforma.c.NoFactura == referencia)).fetchone()
    if not proformaobj:
        return None, conn.execute(facturas.select().where(facturas.c.NoFactura == referencia)).fetchone()
    return proformaobj, None


def update_google_calendar_event(id, horario_row, servicio, facturaobj, proformaobj, direccion, UrlGeoLocalizacion, observaciones, referencia):
    codeCalenderEvent = create_google_calendar_event(
        horario_row, servicio, facturaobj, proformaobj, direccion, UrlGeoLocalizacion, observaciones, referencia)
    conn.execute(programacion.update().where(programacion.c.id == id), {
        "CodeGoogleCalendar": codeCalenderEvent
    })


def notify_update(idUsuarioActualizador, text):
    if idUsuarioActualizador != 1:
        send_message(text)


@strawberry.mutation
def eliminar_programacion(self, id: int,
                          idUsuarioActualizador: Optional[int] = None) -> str:
    event_row = conn.execute(programacion.select().where(
        programacion.c.id == id)).fetchone()
    usuario = get_usuario(idUsuarioActualizador)
    ref_value = get_referencia(event_row.codfactura, event_row.codproforma)

    if event_row and event_row.CodeGoogleCalendar:
        delete_google_calendar_event(event_row.CodeGoogleCalendar)

    resultUpd = conn.execute(programacion.update().where(programacion.c.id == id), {
        "idEstado": 2
    })

    text = f"El usuario *{usuario.nombre}* ELIMINO programación con la referencia: *{ref_value}*. URL: https://alaska-cool-programacion.vercel.app/registerprograming/{id}"
    notify_update(idUsuarioActualizador, text)

    conn.commit()
    return str(resultUpd.rowcount) + " Row(s) updated"


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
                            idDepartamento: Optional[int] = None,
                            idEstadoProgramacion: Optional[int] = None,
                            idUsuarioActualizador: Optional[int] = None) -> str:

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
        "idDepartamento": idDepartamento,
        "idEstadoProgramacion": idEstadoProgramacion,

    })

    usuario = get_usuario(idUsuarioActualizador)
    servicio = get_servicio(codservicio)
    referencia = get_referencia(codfactura, codproforma)
    proformaobj, facturaobj = get_proforma_or_factura(referencia)

    horario_row = conn.execute(horario_programacion.select().where(
        horario_programacion.c.id == idHorarioProgramacion)).fetchone()

    if usuario.idTipoUsuario == TipoUsuario.SupervisorTecnico.value:
        update_google_calendar_event(id, horario_row, servicio, facturaobj,
                                     proformaobj, direccion, UrlGeoLocalizacion, observaciones, referencia)

    ref_value = get_referencia(codfactura, referencia)
    text = f"El usuario *{usuario.nombre}* actualizo programación con la referencia: *{ref_value}*. URL: https://alaska-cool-programacion.vercel.app/registerprograming/{id}"

    notify_update(idUsuarioActualizador, text)

    conn.commit()
    return str(result.rowcount) + " Row(s) updated"


lstProgramacionMutation = [crear_programacion,
                           actualizar_programacion, eliminar_programacion]
