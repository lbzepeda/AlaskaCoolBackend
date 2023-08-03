from strawberry.tools import create_type
from .usuario import *

Mutation = create_type("Mutation", lstUsuarioMutation)
