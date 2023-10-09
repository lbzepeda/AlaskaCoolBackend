import os
from datetime import timedelta

from google.cloud import storage
import strawberry
from strawberry.file_uploads import Upload
from strawberry.types import Info

from conn.db import conn, handle_db_transaction
from models.index import archivo_programacion

GCP_CREDENTIALS = os.environ.get('GCP_CREDENTIALS')
BUCKET_NAME = os.environ.get('BUCKET_NAME')

try:
    client = storage.Client.from_service_account_json(GCP_CREDENTIALS)
    bucket = client.bucket(BUCKET_NAME)
except Exception as e:
    print("******¡Error al establecer conexión con Google Cloud Storage!******")
    print(str(e))# Esto imprimirá todo el rastro del error, lo cual puede ser útil para el diagnóstico
    client, bucket = None, None  # Establece las variables a None para evitar futuras operaciones con ellas

def generate_signed_url(blob: storage.Blob, expiration_time: timedelta = timedelta(hours=1)) -> str:
    # Asegúrate de que tu cuenta de servicio tiene los permisos necesarios para firmar URLs.
    # Por defecto, esta función genera una URL que expira en 1 hora.
    return blob.generate_signed_url(expiration=expiration_time, method='GET')

@strawberry.mutation
@handle_db_transaction
async def cargar_archivo_programacion(self, upload: Upload, idTipoArchivo: int, codProgramacion: str) -> int:
    # **Imprimir información de upload**
    print(f"Nombre del archivo: {upload.filename}")
    print(f"Tipo de contenido: {upload.content_type}")
    
    # Crear un nombre de archivo seguro usando el id
    filename = f"{codProgramacion}_{upload.filename}"

    # Leer el contenido del archivo y subirlo a GCS
    content = await upload.read()
    blob = bucket.blob(filename)
    
    try:
        blob.upload_from_string(content)
        blob.make_public()
        
        print(f"Archivo {filename} subido con éxito a Google Cloud Storage.")
    except Exception as e:
        print(f"Error al subir el archivo {filename} a Google Cloud Storage. Detalle del error: {str(e)}")
        return 0  # Retorna 0 o algún otro valor para indicar que hubo un error.

    # Guardar la ruta del archivo en la base de datos (esto será una URL de GCS)
    path_in_gcs = blob.public_url

    archivoprogramacion = {
        "PathArchivo": path_in_gcs,
        "idTipoArchivo": idTipoArchivo,
        "codProgramacion": codProgramacion,
        "NombreArchivo": filename
    }
    
    try:
        result = conn.execute(archivo_programacion.insert(), archivoprogramacion)
        conn.commit()
        return int(result.inserted_primary_key[0])
    except Exception as e:
        print(f"Error al guardar la ruta del archivo {filename} en la base de datos. Detalle del error: {str(e)}")
        return 0  # Retorna 0 o algún otro valor para indicar que hubo un error.

@strawberry.mutation
@handle_db_transaction
async def crear_archivo_programacion(self, PathArchivo: str, idTipoArchivo: int, codProgramacion:str, info: Info) -> int:
    archivoprogramacion =  {
        "PathArchivo": PathArchivo,
        "idTipoArchivo": idTipoArchivo,
        "codProgramacion": codProgramacion
    }
    result = conn.execute(archivo_programacion.insert(),archivoprogramacion)
    conn.commit()
    return int(result.inserted_primary_key[0])

@strawberry.mutation
@handle_db_transaction
def actualizar_archivo_programacion(self, id:int, PathArchivo: str, idTipoArchivo: int, codProgramacion: str, info: Info) -> str:
    result = conn.execute(archivo_programacion.update().where(archivo_programacion.c.id == id), {
        "PathArchivo": PathArchivo,
        "idTipoArchivo": idTipoArchivo,
        "codProgramacion": codProgramacion
    })
    print(result. returns_rows)
    conn.commit()
    return str(result.rowcount) + " Row(s) updated"

lstArchivoProgramacionMutation = [crear_archivo_programacion, actualizar_archivo_programacion, cargar_archivo_programacion]
