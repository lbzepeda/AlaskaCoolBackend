from fastapi import FastAPI
from controllers.index import usuario
from controllers.index import factura
app = FastAPI()

app.include_router(usuario)
app.include_router(factura)