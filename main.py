from fastapi import FastAPI, Request
from strawberry.fastapi import GraphQLRouter
from fastapi.middleware.cors import CORSMiddleware
import strawberry
from queries.queries import Query
from mutations.mutations import Mutation
from webhook.webhook import WebhookHandler

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/webhook/")
async def webhook_receiver(request: Request):
    return await WebhookHandler.handle_request(request)

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")
