from ariadne import make_executable_schema
from graphql.type.schema import GraphQLSchema

from .types import MAIN_TYPE_DEF, mutation, query
from .category import CATEGORY_TYPE_DEF

def create_schema() -> GraphQLSchema:
    return make_executable_schema([MAIN_TYPE_DEF, CATEGORY_TYPE_DEF], [query, mutation])