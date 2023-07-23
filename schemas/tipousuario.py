from pydantic import BaseModel
class TipoUsuario(BaseModel):
    id: int
    nombe: str
    descripcion: str