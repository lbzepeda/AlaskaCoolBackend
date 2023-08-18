import strawberry
from conn.db import conn
from models.index import archivo_programacion
from strawberry.types import Info

@strawberry.mutation
async def crear_archivo_programacion(self, PathArchivo: str, idTipoArchivo: int, idProgramacion:int, info: Info) -> int:
    archivoprogramacion =  {
        "PathArchivo": PathArchivo,
        "≈": idTipoArchivo,
        "idProgramacion": idProgramacion
    }
    result = conn.execute(archivo_programacion.insert(),archivoprogramacion)
    conn.commit();
    return int(result.inserted_primary_key[0])
@strawberry.mutation
def actualizar_archivo_programacion(self, id:int, PathArchivo: str, idTipoArchivo: int, idProgramacion: int, info: Info) -> str:
    result = conn.execute(archivo_programacion.update().where(archivo_programacion.c.id == id), {
        "PathArchivo": PathArchivo,
        "idTipoArchivo": idTipoArchivo,
        "idProgramacion": idProgramacion
    })
    print(result. returns_rows)
    conn.commit();
    return str(result.rowcount) + " Row(s) updated"

lstArchivoProgramacionMutation = [crear_archivo_programacion, actualizar_archivo_programacion]