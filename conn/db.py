from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://root:9ws9eQ36O8usgsi5s8rL@containers-us-west-64.railway.app:6729/railway', echo=True)
meta = MetaData()
conn = engine.connect()