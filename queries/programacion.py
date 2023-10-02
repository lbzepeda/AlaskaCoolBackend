import typing
import strawberry
from conn.db import conn
from models.index import programacion, productos, proforma, usuarios, usuario_cuadrilla, facturas, horario_programacion, departamentos, estado_programacion, archivo_programacion
from strawberry.types import Info
from typing import Optional
from sqlalchemy import and_
from sqlalchemy.sql import func
from sqlalchemy import select
from datetime import datetime
from .proforma import Proforma
from .factura import Factura
from .productos import Productos
from .usuariocuadrilla import UsuarioCuadrilla
from .horarioprogramacion import HorarioProgramacion
from .departamentos import Departamentos
from .estadoprogramacion import EstadoProgramacion
from .usuario import Usuario
from .archivoprogramacion import ArchivoProgramacion

lstProductos = conn.execute(productos.select()).fetchall()
lstUsuarios = conn.execute(usuarios.select()).fetchall()
lstDepartamentos = conn.execute(departamentos.select()).fetchall()
lstEstadoProgramacion = conn.execute(estado_programacion.select()).fetchall()

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
        matching_factura_query = facturas.select().where(facturas.c.NoFactura == self.codfactura)
        result = conn.execute(matching_factura_query).fetchone()
        return Factura(**dict(result._mapping)) if result else None
    codproforma: Optional[str] = None
    @strawberry.field
    def proforma(self, info: Info) -> Optional[Proforma]:
        matching_proforma_query = proforma.select().where(proforma.c.NoFactura == self.codproforma)
        result = conn.execute(matching_proforma_query).fetchone()
        return Proforma(**dict(result._mapping)) if result else None
    @strawberry.field
    def archivos_programacion(self, info: Info) -> typing.List[Optional[ArchivoProgramacion]]: 
        cod_doc = self.codproforma if self.codproforma else self.codfactura
        matching_factura_query = archivo_programacion.select().where(archivo_programacion.c.codProgramacion == cod_doc)
        result = conn.execute(matching_factura_query).fetchall()
        return [ArchivoProgramacion(**dict(r._mapping)) for r in result] if result else []
    @strawberry.field
    def cantidad_archivos_programacion(self, info: Info) -> int: 
        cod_doc = self.codproforma if self.codproforma else self.codfactura
        result = conn.execute(archivo_programacion.select().where(archivo_programacion.c.codProgramacion == cod_doc)).fetchall()
        return len(result)
    idUsuarioCreacion: int
    @strawberry.field
    def usuario_creacion(self, info: Info) -> Optional[Usuario]:  
        usuariocreador = [Usuario(**dict(usuariocreador._mapping)) for usuariocreador in lstUsuarios if usuariocreador and usuariocreador.id == self.idUsuarioCreacion]
        return usuariocreador[0] if usuariocreador else None
    idCuadrilla: Optional[int] = None
    @strawberry.field
    def cuadrilla(self, info: Info) -> typing.List[Optional[UsuarioCuadrilla]]:
        cuadrillas = conn.execute(usuario_cuadrilla.select().where(usuario_cuadrilla.c.idCuadrilla == self.idCuadrilla)).fetchall()
        return [UsuarioCuadrilla(**dict(cuadrilla._mapping)) for cuadrilla in cuadrillas] or []
    idHorarioProgramacion: Optional[int] = None
    @strawberry.field
    def horarioprogramacion(self, info: Info) -> Optional[HorarioProgramacion]:
        horario = conn.execute(horario_programacion.select().where(horario_programacion.c.id == self.idHorarioProgramacion)).first()
        return HorarioProgramacion(**dict(horario._mapping)) if horario else None
    UrlGeoLocalizacion: str
    direccion: Optional[str]
    observaciones: Optional[str]
    idDepartamento: int
    @strawberry.field
    def departamento(self, info: Info) -> Optional[Departamentos]:  
        departamento = [Departamentos(**dict(departamento._mapping)) for departamento in lstDepartamentos if departamento and departamento.id == self.idDepartamento]
        return departamento[0] if departamento else None
    idEstadoProgramacion: int
    @strawberry.field
    def estado_programacion(self, info: Info) -> Optional[EstadoProgramacion]:  
        estadoprogramacion = [EstadoProgramacion(**dict(estadoprogramacion._mapping)) for estadoprogramacion in lstEstadoProgramacion if estadoprogramacion and estadoprogramacion.id == self.idEstadoProgramacion]
        return estadoprogramacion[0] if estadoprogramacion else None
    idEstado: int
    codeGoogleCalendar: Optional[str]
    FechaCreacion: Optional[datetime] = None
    idTipoProgramacion: int
    nombrecliente: Optional[str] = None
    facturascheque: Optional[str] = None
    @classmethod
    def from_row(cls, row):
        return cls(**row)

@strawberry.field
def programacion_por_id(id: int) -> Optional[Programacion]:
    result = conn.execute(programacion.select().where(and_(programacion.c.id == id, programacion.c.idEstado == 1))).fetchone()
    return result

@strawberry.field
def lista_programacion(
    self,
    page: int = 1,
    perPage: int = 10,
    fechaInicio: Optional[datetime] = None,
    fechaFin: Optional[datetime] = None,
    codServicio: Optional[str] = None,
) -> typing.List[Programacion]:

    offset = (page - 1) * perPage
    query = programacion.select().where(programacion.c.idEstado == 1).order_by(programacion.c.id.desc())

    if fechaInicio and fechaFin:
        query = query.where(and_(programacion.c.FechaCreacion >= fechaInicio, programacion.c.FechaCreacion <= fechaFin))
    
    if codServicio:
        query = query.where(programacion.c.codservicio == codServicio)

    query = query.limit(perPage).offset(offset)
    result = conn.execute(query).fetchall()
    
    return result

@strawberry.field
def cantidad_programacion(
    fechaInicio: Optional[datetime] = None,
    fechaFin: Optional[datetime] = None,
    codServicio: Optional[str] = None
) -> Optional[int]:

    query = programacion.select().where(programacion.c.idEstado == 1)
    if fechaInicio and fechaFin:
        query = query.where(and_(programacion.c.FechaCreacion >= fechaInicio, programacion.c.FechaCreacion <= fechaFin))
    
    if codServicio:
        query = query.where(programacion.c.codservicio == codServicio)
        
    result = conn.execute(query).fetchall()
    
    return len(result)

@strawberry.field
def lista_programacion_excel(
    self,
    page: int = 1,
    perPage: int = 100,
    fechaInicio: Optional[datetime] = None,
    fechaFin: Optional[datetime] = None,
    codServicio: Optional[str] = None,
) -> typing.List[Programacion]:

    offset = (page - 1) * perPage
    query = programacion.select().where(programacion.c.idEstado == 1).order_by(programacion.c.id.desc())

    if fechaInicio and fechaFin:
        query = query.where(and_(programacion.c.FechaCreacion >= fechaInicio, programacion.c.FechaCreacion <= fechaFin))
    
    if codServicio:
        query = query.where(programacion.c.codservicio == codServicio)

    query = query.limit(perPage).offset(offset)
    result = conn.execute(query).fetchall()
    
    return result

@strawberry.field
def cerrar_programacion(id: str) -> bool:
    matching_factura_query_2 = archivo_programacion.select().where(
        (archivo_programacion.c.codProgramacion == id) & 
        (archivo_programacion.c.idTipoArchivo == 2)
    )
    result_2 = conn.execute(matching_factura_query_2).fetchone()
    
    matching_factura_query_1 = archivo_programacion.select().where(
        (archivo_programacion.c.codProgramacion == id) & 
        (archivo_programacion.c.idTipoArchivo == 1)
    )
    result_1 = conn.execute(matching_factura_query_1).fetchone()

    if not result_2 or result_2[0] == 0:
        return False
    elif not result_1 or result_1[0] == 0:
        return False
    else:
        return True


lstProgramacionQuery = [programacion_por_id, lista_programacion, cantidad_programacion, cerrar_programacion, lista_programacion_excel]