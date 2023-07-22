from fastapi import APIRouter
from type.estado import Query
from strawberry.asgi import GraphQL
import strawberry
estado = APIRouter()

schema = strawberry.Schema(Query)
graphql_app = GraphQL(schema)

estado.add_route("/estado", graphql_app)