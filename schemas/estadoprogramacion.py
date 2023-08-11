from pydantic import BaseModel
class EstadoProgramacion(BaseModel):
    id: int
    nombe: str
    descripcion: str