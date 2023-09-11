import typing
import os
import strawberry
from strawberry.file_uploads import Upload
from conn.db import conn
from models.index import archivo_programacion
from strawberry.types import Info
import boto3
import os

AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')
BUCKET_NAME = os.environ.get('BUCKET_NAME')

s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)


@strawberry.mutation
async def cargar_archivo_programacion(self, file: Upload, idTipoArchivo: int, idProgramacion: int) -> int:
    # Crear un nombre de archivo seguro usando el id
    filename = f"{idProgramacion}_{file.filename}"

    # Leer el contenido del archivo y subirlo a S3
    content = await file.read()
    s3.put_object(Bucket=BUCKET_NAME, Key=filename, Body=content)

    # Guardar la ruta del archivo en la base de datos (esto será una URL de S3)
    path_in_s3 = f"https://{BUCKET_NAME}.s3.amazonaws.com/{filename}"
    
    archivoprogramacion = {
        "PathArchivo": path_in_s3,
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