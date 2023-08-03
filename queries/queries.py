from strawberry.tools import create_type
from .usuario import *

Query = create_type("Query", lstUsuarioQuery)
