from fastapi import FastAPI
from controllers.index import usuario, factura, estado
app = FastAPI()

app.include_router(usuario)
app.include_router(factura)
app.include_router(estado)