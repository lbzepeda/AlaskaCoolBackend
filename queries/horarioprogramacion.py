import typing
import strawberry
from conn.db import conn
from models.index import horario_programacion
from datetime import datetime, time

@strawberry.type
class HorarioProgramacion:
    id: int
    fechainicio: datetime
    fechafin: datetime
    horainicio: time
    horafin: time

@strawberry.field
def horario_programacion_por_id(id: int) -> HorarioProgramacion:
    return conn.execute(horario_programacion.select().where(horario_programacion.c.id == id)).fetchone()
@strawberry.field
def lista_horarios_programacion(self) -> typing.List[HorarioProgramacion]:
    return conn.execute(horario_programacion.select()).fetchall()

lstHorarioProductoQuery = [horario_programacion_por_id, lista_horarios_programacion]