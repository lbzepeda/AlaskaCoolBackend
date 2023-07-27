from pydantic import BaseModel
class UsuarioCuadrilla(BaseModel):
    id: int
    idUsuario: int
    idCuadrilla: int