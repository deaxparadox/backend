from django.contrib.auth.models import User 
from rest_framework import generics
from snippets_user.models import SnippetUser
from snippets_user.serializers import SnippetUserSerializers, UserSerializer

class SnippetList(generics.ListCreateAPIView):
    queryset = SnippetUser.objects.all()
    serializer_class = SnippetUserSerializers

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SnippetUser.objects.all()
    serializer_class = SnippetUserSerializers

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer