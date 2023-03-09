from rest_framework import serializers
from taggit.serializers import (
    TagListSerializerField, TaggitSerializer
)

from blog.models import Post 

class BlogSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Post 
        fields = ("title", "slug", "author", "body", "created", "tags")

class BlogCreateSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Post 
        fields = ('title', 'author', 'body', 'tags', "status")
