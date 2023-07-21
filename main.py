from fastapi import FastAPI
from controllers.index import user
from controllers.index import factura
app = FastAPI()

app.include_router(user)
app.include_router(factura)