from sqlalchemy import create_engine, MetaData
import urllib.parse
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Conexión a MySQL
engine = create_engine('mysql+pymysql://root:Carl1991*+1@34.173.53.131:3306/alaskacool', echo=True,
    echo_pool=True,
    pool_use_lifo=True,
    pool_pre_ping=True,
    pool_recycle=3600)
meta = MetaData()
conn = engine.connect()

# Conexión a SQL Server
# connection_string = (
#     "mssql+pyodbc://LZepeda:Zepeda2023@20.120.95.95\\ALASKACOOL/2201ALASKACOOL_CENTRAL"
#     "?driver=ODBC+Driver+17+for+SQL+Server&odbc_connect=" + urllib.parse.quote_plus("DRIVER={/opt/homebrew/Cellar/unixodbc/2.3.12/lib/libodbc.2.dylib};SERVER=20.120.95.95\\ALASKACOOL;DATABASE=2201ALASKACOOL_CENTRAL;UID=LZepeda;PWD=Zepeda2023")
# )

# engine_sql = create_engine(connection_string, echo=True,
# echo_pool=True,
# pool_use_lifo=True,
# pool_pre_ping=True,
# pool_recycle=3600)
# meta_sql = MetaData()

# try:
#     conn_sql = engine_sql.connect()
#     logger.info("Conexión exitosa a SQL Server.")
# except Exception as e:
#     logger.error(f"Error al conectarse a SQL Server: {e}")