from fastapi import APIRouter
from type.programacion import Query, Mutation
from strawberry.asgi import GraphQL
import strawberry
programacion = APIRouter()

schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQL(schema)

programacion.add_route("/programacion", graphql_app)