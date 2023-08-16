import typing
import strawberry
from conn.db import conn
from models.index import programacion, productos, proforma, usuarios, usuario_cuadrilla, facturas, horario_programacion, departamentos, estado_programacion
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