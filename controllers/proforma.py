from fastapi import APIRouter
from type.proforma import Query
from strawberry.asgi import GraphQL
import strawberry
proforma = APIRouter()

schema = strawberry.Schema(Query)
graphql_app = GraphQL(schema)

proforma.add_route("/proforma", graphql_app)