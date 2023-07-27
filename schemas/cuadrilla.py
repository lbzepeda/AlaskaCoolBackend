from pydantic import BaseModel
class Cuadrilla(BaseModel):
    id: int
    nombe: str
    descripcion: str