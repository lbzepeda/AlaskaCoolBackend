from fastapi import FastAPI
from controllers.index import usuario, factura, estado, tipousuario, cuadrilla, usuariocuadrilla, detallefactura, producto, detalleproforma, proforma, horario_programacion
app = FastAPI()

app.include_router(usuario)
app.include_router(factura)
app.include_router(estado)
app.include_router(tipousuario)
app.include_router(cuadrilla)
app.include_router(usuariocuadrilla)
app.include_router(detallefactura)
app.include_router(producto)
app.include_router(detalleproforma)
app.include_router(proforma)
app.include_router(horario_programacion)