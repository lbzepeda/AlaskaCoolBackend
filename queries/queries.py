from strawberry.tools import create_type
from .usuario import *
from .cuadrilla import *

Query = create_type("Query", lstUsuarioQuery + lstCuadrillaQuery)
