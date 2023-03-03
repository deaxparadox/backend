from rest_framework import serializers

from ..models import Post 

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = ("title", "slug", "author", "body", "created")