from pydantic import BaseModel
class Usuario(BaseModel):
    id: int
    nombe: str
    correo: str
    idEstado: int
    idTipoUsuario: int