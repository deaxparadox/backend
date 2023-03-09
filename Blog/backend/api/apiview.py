from rest_framework import generics
from rest_framework.settings import api_settings
from django.utils.text  import slugify

from blog.models import Post
from .serializers import (
    BlogSerializer, BlogCreateSerializer
)

class BlogListView(generics.ListAPIView):
    queryset = Post.published.all()
    serializer_class = BlogSerializer

class BlogCreateView(generics.CreateAPIView):
    serializer_class = BlogCreateSerializer
    queryset = Post.published.all()
 
    def perform_create(self, serializer):
        slug = slugify(self.request.data['title'])
        serializer.save(slug=slug)
