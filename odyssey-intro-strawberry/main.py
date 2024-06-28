from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from api.schema import schema

app = FastAPI()

graphql_router = GraphQLRouter(...,path="/",graphql_ide="apollo-sandbox")
# @app.get("/")
# async def hello_world():
#     return {"message": "Hello World"}

app.include_router(graphql_router)