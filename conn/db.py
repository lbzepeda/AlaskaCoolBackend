from sqlalchemy import create_engine, MetaData

# Conexión a MySQL
engine = create_engine('mysql+pymysql://root:Carl1991*+1@34.173.53.131:3306/alaskacool', echo=True,
    echo_pool=True,
    pool_use_lifo=True,
    pool_pre_ping=True,
    pool_recycle=3600)
meta = MetaData()
conn = engine.connect()

# Conexión a SQL Server
connection_string = (
    "mssql+pymssql://LZepeda:Zepeda2023@20.120.95.95:1433/2201ALASKACOOL_CENTRAL"
)
engine_sql = create_engine(connection_string, echo=True,
    echo_pool=True,
    pool_use_lifo=True,
    pool_pre_ping=True,
    pool_recycle=3600)
meta_sql = MetaData()

conn_sql = engine_sql.connect()