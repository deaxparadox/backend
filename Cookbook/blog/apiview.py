from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from typing import Sequence


from .models import Blog
from .serializers import BlogSerializer, UserSerializer


class BlogsAPIView(generics.ListAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

# class LoginAPIView(generics.ListAPIView):
#     def 

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    authentication_classes: Sequence[str] = ()
    permission_classes: Sequence[str] = ()