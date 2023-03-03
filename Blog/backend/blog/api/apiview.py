from rest_framework import generics

from ..models import Post
from .serializers import BlogSerializer

class BlogListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer