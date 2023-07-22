from pydantic import BaseModel
class Estado(BaseModel):
    id: int
    nombe: str
    descripcion: str