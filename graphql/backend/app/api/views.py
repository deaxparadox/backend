from rest_framework import generics

from ..models import Contact
from .serializers import ContactSerializers

class ListView(generics.ListAPIView):
    serializer_class = ContactSerializers
    queryset = Contact.objects.all()