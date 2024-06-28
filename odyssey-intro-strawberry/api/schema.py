'''
Creating a schema
'''

import strawberry
from .query import Query

schema = strawberry.schema(query=Query)