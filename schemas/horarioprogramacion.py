from pydantic import BaseModel
from datetime import datetime, time

class HorarioProgramacion(BaseModel):
    id: int
    fechainicio: datetime
    fechafin: datetime
    horainicio: time
    horafin: time
