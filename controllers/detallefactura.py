from fastapi import APIRouter
from type.detallefactura import Query
from strawberry.asgi import GraphQL
import strawberry
detallefactura = APIRouter()

schema = strawberry.Schema(Query)
graphql_app = GraphQL(schema)

detallefactura.add_route("/detallefactura", graphql_app)