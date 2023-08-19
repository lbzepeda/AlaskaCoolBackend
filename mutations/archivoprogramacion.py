import typing
import os
import strawberry
from strawberry.file_uploads import Upload
from conn.db import conn
from models.index import archivo_programacion
from strawberry.types import Info

SAVE_PATH = "files/programation/"

@strawberry.mutation
async def cargar_archivo_programacion(self, file: Upload, idTipoArchivo: int, idProgramacion: int) -> int:
    # Crear un nombre de archivo seguro usando el id
    filename = os.path.join(SAVE_PATH, f"{idProgramacion}_{file.filename}")

    # Guardar el archivo en el sistema de archivos
    with open(filename, 'wb') as buffer:
        content = await file.read()
        buffer.write(content)

    # Guardar la ruta del archivo en la base de datos
    archivoprogramacion = {
        "PathArchivo": filename,
        "idTipoArchivo": idTipoArchivo,
        "idProgramacion": idProgramacion
    }
    result = conn.execute(archivo_programacion.insert(), archivoprogramacion)
    conn.commit()
    return int(result.inserted_primary_key[0])

@strawberry.mutation
async def crear_archivo_programacion(self, PathArchivo: str, idTipoArchivo: int, idProgramacion:int, info: Info) -> int:
    archivoprogramacion =  {
        "PathArchivo": PathArchivo,
        "idTipoArchivo": idTipoArchivo,
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

lstArchivoProgramacionMutation = [crear_archivo_programacion, actualizar_archivo_programacion, cargar_archivo_programacion]