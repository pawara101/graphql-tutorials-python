import strawberry

def get_hello():
    return "Hello from Query"

@strawberry.type ## To define as it is Graphql type
class Query:
    
    hello: str = strawberry.field(resolver=get_hello) ## resolver