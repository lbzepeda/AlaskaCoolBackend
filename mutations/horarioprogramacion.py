import strawberry
from conn.db import conn
from models.index import horario_programacion
from strawberry.types import Info
from datetime import datetime, time

@strawberry.type
class HorarioProgramacion:
    id: int
    fechainicio: datetime
    fechafin: datetime
    horainicio: time
    horafin: time

@strawberry.mutation
async def crear_horario_programacion(self, fechainicio: datetime, fechafin: datetime, horainicio: time, horafin: time, info: Info) -> int:
    tipousuario =  {
        "fechainicio": fechainicio,
        "fechafin": fechafin,
        "horainicio": horainicio,
        "horafin": horafin
    }
    result = conn.execute(horario_programacion.insert(),tipousuario)
    conn.commit();
    return int(result.inserted_primary_key[0])
@strawberry.mutation
def actualizar_horario_programacion(self, id:int, fechainicio: datetime, fechafin: datetime, horainicio: time, horafin: time, info: Info) -> str:
    result = conn.execute(horario_programacion.update().where(horario_programacion.c.id == id), {
        "fechainicio": fechainicio,
        "fechafin": fechafin,
        "horainicio": horainicio,
        "horafin": horafin
    })
    print(result. returns_rows)
    conn.commit();
    return str(result.rowcount) + " Row(s) updated"

lstHorarioProgramacionMutation = [crear_horario_programacion, actualizar_horario_programacion]