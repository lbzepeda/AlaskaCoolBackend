from pydantic import BaseModel
class TipoArchivo(BaseModel):
    id: int
    nombe: str
    descripcion: str