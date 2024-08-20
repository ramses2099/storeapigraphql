from ariadne import MutationType, QueryType

MAIN_TYPE_DEF = """
    type Query {
        categories: [Category]
        category(id: ID!): Category!
"""

query = QueryType()
mutation = MutationType()