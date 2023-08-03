from strawberry.tools import create_type
from .usuario import *
from .cuadrilla import *

Mutation = create_type("Mutation", lstUsuarioMutation + lstCuadrillaMutation)
