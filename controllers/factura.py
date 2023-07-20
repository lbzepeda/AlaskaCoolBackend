from fastapi import APIRouter
from type.factura import Query
from strawberry.asgi import GraphQL
import strawberry
factura = APIRouter()

schema = strawberry.Schema(Query)
graphql_app = GraphQL(schema)

factura.add_route("/graphql", graphql_app)