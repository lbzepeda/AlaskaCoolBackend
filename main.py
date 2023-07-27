from fastapi import FastAPI
from controllers.index import usuario, factura, estado, tipousuario, cuadrilla
app = FastAPI()

app.include_router(usuario)
app.include_router(factura)
app.include_router(estado)
app.include_router(tipousuario)
app.include_router(cuadrilla)