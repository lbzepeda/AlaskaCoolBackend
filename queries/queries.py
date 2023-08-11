from strawberry.tools import create_type
from .usuario import *
from .cuadrilla import *
from .detallefactura import *
from .detalleproforma import *
from .factura import *
from .productos import *
from .proforma import *
from .tipousuario import *
from .usuariocuadrilla import *
from .horarioprogramacion import *
from .programacion import *
from .departamentos import *
from .estadoprogramacion import * 

Query = create_type("Query", lstUsuarioQuery + lstCuadrillaQuery + lstDetalleFacturaQuery + lstDetalleProformaQuery + lstFacturaQuery + lstProductoQuery
                    + lstProformaQuery + lstTipoUsuarioQuery + lstUsuarioCuadrillaQuery + lstHorarioProductoQuery + lstProgramacionQuery + lstDepartamentosQuery + lstEstadoProgramacionQuery)
