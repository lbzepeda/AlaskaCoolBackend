from strawberry.tools import create_type
from .usuario import *
from .cuadrilla import *
from .tipousuario import *
from .usuariocuadrilla import *
from .horarioprogramacion import *
from .programacion import *
from .archivoprogramacion import *

Mutation = create_type("Mutation", lstUsuarioMutation + lstCuadrillaMutation + lstTipoUsuarioMutation + lstUsuarioCuadrillaMutation
                       + lstHorarioProgramacionMutation + lstProgramacionMutation + lstArchivoProgramacionMutation)
