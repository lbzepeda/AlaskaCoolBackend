from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://root:Carl1991*+1@34.173.53.131:3306/alaskacool', echo=True)
meta = MetaData()
conn = engine.connect()