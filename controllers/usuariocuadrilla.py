from fastapi import APIRouter
from type.usuariocuadrilla import Query, Mutation
from strawberry.asgi import GraphQL
import strawberry
usuariocuadrilla = APIRouter()

schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQL(schema)

usuariocuadrilla.add_route("/usuariocuadrilla", graphql_app)