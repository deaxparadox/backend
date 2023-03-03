import graphene
from graphene_django import DjangoObjectType

from ..models import Blog

class BlogType(DjangoObjectType):
    class Meta:
        model = Blog
        fields = ("title", "content", "date_time")

class BlogQuery(graphene.ObjectType):
    blogs = graphene.List(BlogType)

    def resolve_blogs(self, info, **kwargs):
        return Blog.objects.all()