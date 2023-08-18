from pydantic import BaseModel
class ArchivoProgramacion(BaseModel):
    id: int
    PathArchivo: str
    idTipoArchivo: int