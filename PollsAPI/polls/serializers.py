from rest_framework import serializers
from rest_framework.authtoken.models import Token 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


from typing import Sequence

from .models import Poll, Choice, Vote 

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote 
        fields = "__all__"

class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)
    class Meta:
        model = Choice
        fields = "__all__"

class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Poll
        fields = "__all__"

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

