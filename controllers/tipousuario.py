from fastapi import APIRouter
from type.tipousuario import Query, Mutation
from strawberry.asgi import GraphQL
import strawberry
tipousuario = APIRouter()

schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQL(schema)

tipousuario.add_route("/tipousuario", graphql_app)