from rest_framework import generics

from . import serializers
from app import models

class Todo(generics.ListAPIView):
    queryset = models.Todo.object.all()
    serializer_class = serializers.TodoSerializer