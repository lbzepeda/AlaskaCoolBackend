from fastapi import APIRouter
from type.cuadrilla import Query, Mutation
from strawberry.asgi import GraphQL
import strawberry
cuadrilla = APIRouter()

schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQL(schema)

cuadrilla.add_route("/cuadrilla", graphql_app)