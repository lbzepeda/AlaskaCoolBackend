import os
from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# ------- Configuración de SQL -------
DB_USERNAME_SQL = os.getenv('DB_USERNAME_SQL')
DB_PASSWORD_SQL = os.getenv('DB_PASSWORD_SQL')
DB_HOST_SQL = os.getenv('DB_HOST_SQL')
DB_NAME_SQL = os.getenv('DB_NAME_SQL')
DB_DRIVER_SQL = os.getenv('DB_DRIVER_SQL')

connection_string = (
    f"mssql+pyodbc://{DB_USERNAME_SQL}:{DB_PASSWORD_SQL}@"
    f"{DB_HOST_SQL}/{DB_NAME_SQL}?driver={DB_DRIVER_SQL}"
)

engine_sql = create_engine(
    connection_string, 
    echo=True, echo_pool=True, pool_use_lifo=True,
    pool_pre_ping=True, pool_recycle=3600
)

meta_sql = MetaData()
conn_sql = engine_sql.connect()

# ------- Configuración de MySQL -------
DB_USERNAME_MYSQL = os.getenv('DB_USERNAME_MYSQL')
DB_PASSWORD_MYSQL = os.getenv('DB_PASSWORD_MYSQL')
DB_HOST_MYSQL = os.getenv('DB_HOST_MYSQL')
DB_NAME_MYSQL = os.getenv('DB_NAME_MYSQL')
DB_PORT_MYSQL = os.getenv('DB_PORT_MYSQL')

connection_string_mysql = (
    f"mysql+pymysql://{DB_USERNAME_MYSQL}:{DB_PASSWORD_MYSQL}@"
    f"{DB_HOST_MYSQL}:{DB_PORT_MYSQL}/{DB_NAME_MYSQL}"
)

engine = create_engine(
    connection_string_mysql, 
    echo=True, echo_pool=True, pool_use_lifo=True,
    pool_pre_ping=True, pool_recycle=3600,
    pool_size=10,
    max_overflow=5,
    pool_timeout=30
)

meta = MetaData()
conn = engine.connect()
