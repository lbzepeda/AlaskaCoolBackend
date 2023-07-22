from fastapi import APIRouter
from type.usuario import Mutation, Query
from strawberry.asgi import GraphQL
import strawberry
usuario = APIRouter()

schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQL(schema)

usuario.add_route("/usuario", graphql_app)