from .types import query
from graphql import GraphQLResolveInfo
from ..models import Category
from ..operations import get_all_categories, get_category_by_id

CATEGORY_TYPE_DEF = """
    type Category {
        id: ID!
        description: String!
        user_id: ID!
        updated: DateTime
        created: DateTime
    }
"""

@query.field("categories")
def resolve_categories(_, info:GraphQLResolveInfo) -> list[Category]:
    return get_all_categories()
    
@query.field("category")
def resolve_categories(_, info:GraphQLResolveInfo, id: int) -> Category:
    return get_category_by_id(id)
    
