from fastapi import APIRouter
from type.productos import Query
from strawberry.asgi import GraphQL
import strawberry
producto = APIRouter()

schema = strawberry.Schema(Query)
graphql_app = GraphQL(schema)

producto.add_route("/producto", graphql_app)