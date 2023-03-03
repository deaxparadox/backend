from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from taggit.serializers import (
    TagListSerializerField, TaggitSerializer
)
from typing import Sequence

from .models import Blog

class BlogSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model: Blog = Blog 
        fields: Sequence[str] = ('title', 'content', "tags", 'date_time')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model: User  = User 
        fields: Sequence[list] = ('username', 'email', 'password')
        extra_kwargs: dict = {
            "password": {
                "write_only": True,
            }
        }

    def create(self, validate_data):
        user = User(
            email=validate_data["email"],
            username=validate_data['username']
        )
        user.set_password(validate_data["password"])
        user.save()
        Token.objects.create(user=user)
        return user 
