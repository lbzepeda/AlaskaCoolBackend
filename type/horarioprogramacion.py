import typing
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
    
@strawberry.type
class Query:
    @strawberry.field
    def horario_programacion(id: int) -> HorarioProgramacion:
        return conn.execute(horario_programacion.select().where(horario_programacion.c.id == id)).fetchone()
    @strawberry.field
    def horarios_programacion(self) -> typing.List[HorarioProgramacion]:
        return conn.execute(horario_programacion.select()).fetchall()
    
@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_horario_programacion(self, fechainicio: datetime, fechafin: datetime, horainicio: time, horafin: time, info: Info) -> int:
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
    def update_horario_programacion(self, id:int, fechainicio: datetime, fechafin: datetime, horainicio: time, horafin: time, info: Info) -> str:
        result = conn.execute(horario_programacion.update().where(horario_programacion.c.id == id), {
            "fechainicio": fechainicio,
            "fechafin": fechafin,
            "horainicio": horainicio,
            "horafin": horafin
        })
        print(result. returns_rows)
        conn.commit();
        return str(result.rowcount) + " Row(s) updated"
    
