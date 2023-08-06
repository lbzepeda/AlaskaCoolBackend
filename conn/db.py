from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://root:Carl1991*+1@34.173.53.131:3306/alaskacool', echo=True, query_cache_size=0)
meta = MetaData()
conn = engine.connect()