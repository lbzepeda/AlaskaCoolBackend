import typing
import strawberry
from conn.db import conn
from models.index import programacion, productos, proforma, det_proforma, usuarios, cuadrillas, usuario_cuadrilla, facturas, det_facturas, horario_programacion, departamentos, estado_programacion
from strawberry.types import Info
from typing import Optional
from .proforma import Proforma
from .factura import Factura
from .productos import Productos
from .usuariocuadrilla import UsuarioCuadrilla
from .horarioprogramacion import HorarioProgramacion
from .departamentos import Departamentos
from .estadoprogramacion import EstadoProgramacion
from .usuario import Usuario

@strawberry.type
class Programacion:
    id: int
    codservicio: str
    @strawberry.field
    def servicio(self, info: Info) -> typing.List[Optional[Productos]]:
        matching_products_query = productos.select().where(productos.c.CodProducto == self.codservicio)
        result = conn.execute(matching_products_query).fetchall()
        return [Productos(**dict(producto._mapping)) for producto in result]
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
    idUsuarioCreacion: int
    @strawberry.field
    def usuario_creacion(self, info: Info) -> Optional[Usuario]:
        usuario = conn.execute(usuarios.select().where(usuarios.c.id == self.idUsuarioCreacion)).first()
        return Usuario(**dict(usuario._mapping)) if usuario else None
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
        departamento = conn.execute(departamentos.select().where(departamentos.c.id == self.idDepartamento)).first()
        return Departamentos(**dict(departamento._mapping)) if departamento else None
    idEstadoProgramacion: int
    @strawberry.field
    def estado_programacion(self, info: Info) -> Optional[EstadoProgramacion]:
        estado = conn.execute(estado_programacion.select().where(estado_programacion.c.id == self.idEstadoProgramacion)).first()
        return EstadoProgramacion(**dict(estado._mapping)) if estado else None
    @classmethod
    def from_row(cls, row):
        return cls(**row)

@strawberry.field
def programacion_por_id(id: int) -> Optional[Programacion]:
    result = conn.execute(programacion.select().where(programacion.c.id == id)).fetchone()
    conn.commit()
    return result

@strawberry.field
def lista_programacion(self) -> typing.List[Programacion]:
    result = conn.execute(programacion.select()).fetchall()
    conn.commit()
    return result

lstProgramacionQuery = [programacion_por_id, lista_programacion]