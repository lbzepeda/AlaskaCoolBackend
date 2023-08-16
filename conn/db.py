from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://root:Carl1991*+1@34.173.53.131:3306/alaskacool', echo=True,
    echo_pool=True,
    pool_use_lifo=True,
    pool_pre_ping=True,
    pool_recycle=3600)
meta = MetaData()
conn = engine.connect()