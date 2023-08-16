from pydantic import BaseModel
from typing import Optional

class Programacion(BaseModel):
    id: int
    codservicio: str
    codcliente: Optional[str] = None
    codfactura: Optional[str] = None
    codproforma: Optional[str] = None
    idUsuarioCreacion: int
    idCuadrilla: Optional[int] = None
    idHorarioProgramacion: Optional[int] = None
    UrlGeoLocalizacion: str
    direccion: Optional[int]
    observaciones: Optional[str] = None
    idEstado: Optional[int] = None
    codeGoogleCalendar: Optional[str] = None
