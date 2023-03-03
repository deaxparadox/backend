import graphene
from graphene_django import DjangoObjectType
from typing import Sequence

from blog.graphql.schema import BlogQuery 
from ingredients.models import Category, Ingredient

class CategoryType(DjangoObjectType):
    class Meta:
        model: Category = Category
        fields: Sequence[str] = ("id", "name", "ingredients")

    
class IngredientType(DjangoObjectType):
    class Meta:
        model: Ingredient = Ingredient
        fields: Sequence[str] = ("id", "name", "notes", "category")

class Query(BlogQuery, graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    category_by_name = graphene.Field(
        CategoryType,
        name=graphene.String(required=True)
    )

    def resolve_all_ingredients(root, info):
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None 

schema = graphene.Schema(query=Query)