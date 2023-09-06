from sqlalchemy import create_engine, MetaData
import pyodbc
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

# Conexión a SQL Server con pymssql
# Nota: Asegúrate de cambiar YOUR_USERNAME y YOUR_PASSWORD por tus credenciales de SQL Server Authentication.
# conn_sql = pyodbc.connect(
#     "Driver={ODBC Driver 17 for SQL Server}",
#     server="20.120.95.95\ALASKACOOL",
#     user="LZepeda",
#     password="Zepeda2023",
#     database="2201ALASKACOOL_CENTRAL",
#     schema="ALASKACOOL_Lectura",
#     sslmode="no_verify"
# )

# connection_string = (
#     "mssql+pyodbc://LZepeda:Zepeda2023@20.120.95.95\ALASKACOOL/2201ALASKACOOL_CENTRAL?"
#     "driver=ODBC+Driver+17+for+SQL+Server&sslmode=no_verify"
# )

connection_string = (
    'mssql+pyodbc://LZepeda:Zepeda2023@20.120.95.95\ALASKACOOL/2201ALASKACOOL_CENTRAL?driver=ODBC+Driver+17+for+SQL+Server'
)

engine_sql = create_engine(connection_string, echo=True,
    echo_pool=True,
    pool_use_lifo=True,
    pool_pre_ping=True,
    pool_recycle=3600)

meta_sql = MetaData()

# Crear una conexión
conn_sql = engine_sql.connect()