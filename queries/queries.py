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
from .tipoarchivo import *
from .archivoprogramacion import *
from .tipoprogramacion import *
from .bancos import *
from .clientes import *
from .cargo import *
from .genero import *
from .moneda import *
from .colaboradores import *
from .contratacioncolaboradores import *
from .esquemapago import *
from .tipopago import *
from .fechapago import *

Query = create_type("Query", lstUsuarioQuery + lstCuadrillaQuery + lstDetalleFacturaQuery + lstDetalleProformaQuery + lstFacturaQuery + lstProductoQuery
                    + lstProformaQuery + lstTipoUsuarioQuery + lstUsuarioCuadrillaQuery + lstHorarioProductoQuery + lstProgramacionQuery + lstDepartamentosQuery + lstEstadoProgramacionQuery + lstTipoArchivoQuery + lstArchivoProgramacionQuery
                    + lstTipoProgramacionQuery + lstBancoQuery + lstClienteQuery + lstCargoQuery + lstGeneroQuery + lstMonedaQuery + lstColaboradoresQuery + lstContratacionColaboradoresQuery + lstEsquemaPagoQuery + lstTipoPagoQuery + lstFechaPagoQuery)
