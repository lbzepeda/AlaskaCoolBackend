from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from fastapi.middleware.cors import CORSMiddleware
#from controllers.index import usuario, factura, estado, tipousuario, cuadrilla, usuariocuadrilla, detallefactura, producto, detalleproforma, proforma, horario_programacion, programacion
import strawberry
from queries.queries import Query
from mutations.mutations import Mutation
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)
app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")