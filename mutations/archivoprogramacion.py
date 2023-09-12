import typing
import os
import strawberry
from strawberry.file_uploads import Upload
from conn.db import conn
from models.index import archivo_programacion
from strawberry.types import Info
from google.cloud import storage
import os

GCP_CREDENTIALS = os.environ.get('GCP_CREDENTIALS') # Ruta al archivo JSON de credenciales
BUCKET_NAME = os.environ.get('BUCKET_NAME')

try:
    client = storage.Client.from_service_account_json(GCP_CREDENTIALS)
    bucket = client.bucket(BUCKET_NAME)
except Exception as e:
    print("******¡Error al establecer conexión con Google Cloud Storage!******")
    print(str(e))# Esto imprimirá todo el rastro del error, lo cual puede ser útil para el diagnóstico
    client, bucket = None, None  # Establece las variables a None para evitar futuras operaciones con ellas


@strawberry.mutation
async def cargar_archivo_programacion(self, upload: Upload, idTipoArchivo: int, idProgramacion: int) -> int:
    # **Imprimir información de upload**
    print(f"Nombre del archivo: {upload}")
    print(f"Tipo de contenido: {upload.content_type}")
    # Si necesitas más detalles, puedes agregar más líneas de print aquí
    
    # Crear un nombre de archivo seguro usando el id
    filename = f"{idProgramacion}_{upload.filename}"  # Nota: Modifiqué esta línea para usar 'upload.filename'

    # Leer el contenido del archivo y subirlo a GCS
    content = await upload.read()
    blob = bucket.blob(filename)  # **Crear un objeto blob (es similar a un objeto en S3)**
    blob.upload_from_string(content)

    # Guardar la ruta del archivo en la base de datos (esto será una URL de GCS)
    path_in_gcs = blob.public_url  # **Obtener URL pública del archivo en GCS**

    archivoprogramacion = {
        "PathArchivo": path_in_gcs,
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
