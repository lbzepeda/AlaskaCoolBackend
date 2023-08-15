import strawberry
from typing import Optional
from conn.db import conn
import typing
from models.index import departamentos
import strawberry

@strawberry.type
class Departamentos:
    id: int
    nombre: str

@strawberry.field
def departamento_por_id(id: int) -> Optional[Departamentos]:
    result = conn.execute(departamentos.select().where(departamentos.c.id == id)).fetchone()
    conn.commit()
    return result

@strawberry.field
def lista_departamentos(self) -> typing.List[Departamentos]:
    result = conn.execute(departamentos.select()).fetchall()
    conn.commit()
    return result

lstDepartamentosQuery = [departamento_por_id, lista_departamentos]