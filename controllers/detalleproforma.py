from fastapi import APIRouter
from type.detalleproforma import Query
from strawberry.asgi import GraphQL
import strawberry
detalleproforma = APIRouter()

schema = strawberry.Schema(Query)
graphql_app = GraphQL(schema)

detalleproforma.add_route("/detalleproforma", graphql_app)