import strawberry
from conn.db import conn, handle_db_transaction
from models.index import programacion, productos, proforma, det_proforma, usuarios, cuadrillas, usuario_cuadrilla, facturas, det_facturas, horario_programacion
from strawberry.types import Info
from datetime import datetime
from typing import Optional
import os
import ssl
from dotenv import load_dotenv
from datetime import time
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from enum import Enum
from json import dumps
from httplib2 import Http
import pytz
from .programacion import programacion


class TipoUsuario(Enum):
    Tecnico = 1
    Ayudante = 2
    GerenteDeVenta = 3
    Vendedor = 4
    SupervisorTecnico = 5

class TipoProgramacion(Enum):
    Operaciones_Tecnicas = 1
    Retiro_Cheque = 2
    Deposito_Bancario = 3
    Entrega_Equipo = 4
    Retiro_Retencion = 5

tipo_programacion_map = {
    TipoProgramacion.Operaciones_Tecnicas: "Operaciones Técnicas",
    TipoProgramacion.Retiro_Cheque: "Retiro de Cheque",
    TipoProgramacion.Deposito_Bancario: "Depósito Bancario",
    TipoProgramacion.Entrega_Equipo: "Entrega de Equipo",
    TipoProgramacion.Retiro_Retencion: "Retiro de Retención"
}

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


def create_google_calendar_event(horario_row, servicio, facturaobj, proformaobj, direccion, UrlGeoLocalizacion, observaciones, referencia, id):
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
        'summary': f"{cliente} - {servicio.descripcion} - Referencia: {referencia}",
        # Puedes personalizar este texto
        'description': f"URL de Programación: https://alaskacoolprogramacion-production.up.railway.app/registerprograming/{id}\nDireccion: {direccion}\nLocalización: {UrlGeoLocalizacion}\nObservaciones: {observaciones}",
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
    url = webhook_programing
    app_message = {
        'text': text
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
class Programacion:
    id: int
    codservicio: str
    codcliente: Optional[str] = None
    codfactura: Optional[str] = None
    codproforma: Optional[str] = None
    idUsuarioCreacion: int
    idDepartamento: Optional[int] = None
    idCuadrilla: Optional[int] = None
    idHorarioProgramacion: Optional[int] = None
    idEstadoProgramacion: Optional[int] = None
    CodeGoogleCalendar: Optional[str] = None
    UrlGeoLocalizacion: str
    direccion: Optional[int]
    observaciones: Optional[str] = None
    idEstado: Optional[int] = None
    codeGoogleCalendar: Optional[str] = None
    FechaCreacion: Optional[datetime] = None
    idTipoProgramacion: Optional[int] = None
    nombrecliente: Optional[str] = None
    facturascheque: Optional[str] = None

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
@handle_db_transaction
async def crear_programacion(
        self,
        codservicio: Optional[str],
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
        idEstadoProgramacion: Optional[int] = None,
        idTipoProgramacion: Optional[int] = None,
        nombrecliente: Optional[str] = None,
        facturascheque: Optional[str] = None) -> int:
    
    utc_now = datetime.now(pytz.utc)
    current_time_utc_6 = utc_now.astimezone(pytz.timezone('Etc/GMT+6'))

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
        "idHorarioProgramacion": idHorarioProgramacion,
        "FechaCreacion": current_time_utc_6,
        "idTipoProgramacion": idTipoProgramacion,
        "nombrecliente": nombrecliente,
        "facturascheque": facturascheque,
        "idEstado": 1
    }
    result = conn.execute(programacion.insert(), data_programacion)

    id_value = result.inserted_primary_key[0]
    generate_and_send_notification(data_programacion, id_value, conn, 1, 0)

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
        horario_row, servicio, facturaobj, proformaobj, direccion, UrlGeoLocalizacion, observaciones, referencia, id)
    conn.execute(programacion.update().where(programacion.c.id == id), {
        "CodeGoogleCalendar": codeCalenderEvent
    })

def notify_update(idUsuarioActualizador, text):
    # if idUsuarioActualizador != 1:
    send_message(text)

@strawberry.mutation
@handle_db_transaction
def eliminar_programacion(self, id: int, idUsuarioActualizador: Optional[int] = None) -> str:
    
    event_row = conn.execute(programacion.select().where(
        programacion.c.id == id)).fetchone()
    usuario = get_usuario(idUsuarioActualizador)
    ref_value = get_referencia(event_row.codfactura, event_row.codproforma)

    if event_row and event_row.CodeGoogleCalendar:
        delete_google_calendar_event(event_row.CodeGoogleCalendar)

    resultUpd = conn.execute(programacion.update().where(programacion.c.id == id), {
        "idEstado": 2
    })

    text = f"El usuario *{usuario.nombre}* ELIMINO programación con la referencia: *{ref_value}*. URL: https://alaskacoolprogramacion-production.up.railway.app/registerprograming/{id}"
    notify_update(idUsuarioActualizador, text)

    conn.commit()
    return str(resultUpd.rowcount) + " Row(s) updated"

@strawberry.mutation
@handle_db_transaction
def actualizar_programacion(self, id: int,
                            codservicio: Optional[str],
                            # idUsuarioCreacion: Optional[int],
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
                            idUsuarioActualizador: Optional[int] = None,
                            idTipoProgramacion: Optional[int] = None,
                            nombrecliente: Optional[str] = None,
                            facturascheque: Optional[str] = None) -> str:

    result = conn.execute(programacion.update().where(programacion.c.id == id), {
        "codservicio": codservicio,
        # "idUsuarioCreacion": idUsuarioCreacion,
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
        "idTipoProgramacion": idTipoProgramacion,
        "nombrecliente": nombrecliente,
        "facturascheque": facturascheque,
    })

    data_programacion = {
        "codservicio": codservicio,
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
        "idTipoProgramacion": idTipoProgramacion,
        "nombrecliente": nombrecliente,
        "facturascheque": facturascheque,
    }

    generate_and_send_notification(data_programacion, id, conn, 2, idUsuarioActualizador)

    conn.commit()
    return str(result.rowcount) + " Row(s) updated"

@strawberry.mutation
@handle_db_transaction
def cerrar_programacion(self, id: int, idUsuarioActualizador: int) -> str:
    programacion_row = conn.execute(programacion.select().where(
        programacion.c.id == id)).fetchone()
    resultProgramacion= Programacion.from_row(programacion_row)
    usuario = get_usuario(idUsuarioActualizador)

    resultUpd = conn.execute(programacion.update().where(programacion.c.id == id), {
        "idEstadoProgramacion": 3
    })

    text = f"El usuario *{usuario.nombre}* FINALIZÓ programación con la referencia: *{get_referencia(resultProgramacion.codfactura, resultProgramacion.codproforma)}*. URL: https://alaskacoolprogramacion-production.up.railway.app/registerprograming/{id}"
    notify_update(idUsuarioActualizador, text)

    conn.commit()
    return str(resultUpd.rowcount) + " Row(s) updated"

def generate_and_send_notification(data_programacion, id_value, conn, estado, idUsuarioActualizador):
    base_url = "https://alaskacoolprogramacion-production.up.railway.app/registerprograming"
    full_url = f"{base_url}/{id_value}"

    idUsuarioCreacion = data_programacion.get("idUsuarioCreacion") if estado == 1 else idUsuarioActualizador
    codservicio = data_programacion.get("codservicio")
    idTipoProgramacion = data_programacion.get("idTipoProgramacion")
    codfactura = data_programacion.get("codfactura")
    codproforma = data_programacion.get("codproforma")
    
    usuario_row = conn.execute(usuarios.select().where(
        usuarios.c.id == idUsuarioCreacion)).fetchone()
    usuario = Usuario.from_row(usuario_row)

    tipo_programacion_str = tipo_programacion_map.get(
        TipoProgramacion(idTipoProgramacion), "Desconocido")

    accion = "creó" if estado == 1 else "actualizó"
    text = f"El usuario *{usuario.nombre}* {accion} una nueva programación. Tipo de Programación: *{tipo_programacion_str}*"
    
    if TipoProgramacion(idTipoProgramacion) == TipoProgramacion.Operaciones_Tecnicas:

        servicio = get_servicio(codservicio)
        referencia = get_referencia(codfactura, codproforma)
        proformaobj, facturaobj = get_proforma_or_factura(referencia)

        if usuario.idTipoUsuario == TipoUsuario.SupervisorTecnico.value:
            horario_row = conn.execute(horario_programacion.select().where(
            horario_programacion.c.id == data_programacion.get("idHorarioProgramacion"))).fetchone()
        
            servicio_row = conn.execute(productos.select().where(
                productos.c.CodProducto == codservicio)).fetchone()
            servicio = Productos.from_row(servicio_row)

            update_google_calendar_event(id_value, horario_row, servicio, facturaobj,
                                        proformaobj, data_programacion.get("direccion"), data_programacion.get("UrlGeoLocalizacion"), 
                                        data_programacion.get("observaciones"), referencia)
        
        text += f", para el servicio *{servicio.descripcion}*, Ref: *{referencia}*. Registro pendiente de asignación de horario y cuadrilla. URL: {full_url}"

    if TipoProgramacion(idTipoProgramacion) == TipoProgramacion.Retiro_Cheque:
        text += f" URL: {full_url}"
        
    if idUsuarioCreacion == 1:
        return

    send_message(text)

lstProgramacionMutation = [crear_programacion,
                           actualizar_programacion, eliminar_programacion, cerrar_programacion]
