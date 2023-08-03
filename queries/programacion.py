import typing
import strawberry
from conn.db import conn
from models.index import programacion, productos, proforma, det_proforma, usuarios, cuadrillas, usuario_cuadrilla, facturas, det_facturas, horario_programacion
from strawberry.types import Info
from typing import Optional
from .proforma import Proforma
from .factura import Factura
from .productos import Productos
from .usuariocuadrilla import UsuarioCuadrilla
from .horarioprogramacion import HorarioProgramacion

lstProductos = conn.execute(productos.select()).fetchall()
lstProforma = conn.execute(proforma.select()).fetchall()
lstDetProformas = conn.execute(det_proforma.select()).fetchall()
lstUsuarios = conn.execute(usuarios.select()).fetchall()
lstCuadrillas = conn.execute(cuadrillas.select()).fetchall()
lstUsuario_Cuadrilla = conn.execute(usuario_cuadrilla.select()).fetchall()
lstFacturas = conn.execute(facturas.select()).fetchall()
lstDetFacturas = conn.execute(det_facturas.select()).fetchall()
lstHorarioProgramacion = conn.execute(horario_programacion.select()).fetchall()

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
    @strawberry.field
    def horarioprogramacion(self, info: Info) -> Optional[HorarioProgramacion]:  
        horarioprogramacion = [HorarioProgramacion(**dict(horarioprogramacion._mapping)) for horarioprogramacion in lstHorarioProgramacion if horarioprogramacion and horarioprogramacion.id == self.idHorarioProgramacion]
        return horarioprogramacion[0] if horarioprogramacion else None
    UrlGeoLocalizacion: str
    direccion: Optional[str]
    observaciones: Optional[str]
    @classmethod
    def from_row(cls, row):
        return cls(**row)

@strawberry.field
def programacion_por_id(id: int) -> Optional[Programacion]:
    return conn.execute(programacion.select().where(programacion.c.id == id)).fetchone()

@strawberry.field
def lista_programacion(self) -> typing.List[Programacion]:
    return conn.execute(programacion.select()).fetchall()

lstProgramacionQuery = [programacion_por_id, lista_programacion]