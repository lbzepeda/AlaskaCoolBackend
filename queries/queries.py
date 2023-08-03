from strawberry.tools import create_type
from .usuario import *
from .cuadrilla import *
from .detallefactura import *
from .detalleproforma import *

Query = create_type("Query", lstUsuarioQuery + lstCuadrillaQuery + lstDetalleFacturaQuery + lstDetalleProformaQuery)
