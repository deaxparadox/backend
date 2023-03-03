import graphene

import shortener.schema

class Query(shortener.schema.Query):
    pass 

class Mutation(shortener.schema.Mutation, graphene.ObjectType):
    pass 

schema = graphene.Schema(query=Query, mutation=Mutation)