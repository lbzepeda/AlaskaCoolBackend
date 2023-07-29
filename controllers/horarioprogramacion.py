from fastapi import APIRouter
from type.horarioprogramacion import Query, Mutation
from strawberry.asgi import GraphQL
import strawberry
horario_programacion = APIRouter()

schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQL(schema)

horario_programacion.add_route("/horarioprogramacion", graphql_app)