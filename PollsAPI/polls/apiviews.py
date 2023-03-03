from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate

import rich 
from rich.panel import Panel 
from rich.text import Text 


from .models import Poll, Choice
from .serializers import (
    PollSerializer, ChoiceSerializer, VoteSerializer, UserSerializer
)
# class PollList(APIView):
#     def get(self, request):
#         polls = Poll.objects.all()
#         serializer = PollSerializer(polls, many=True)
#         return Response(serializer.data)

# class PollDetail(APIView):
#     def get(self, request, pk):
#         polls = get_object_or_404(Poll, pk=pk)
#         data = PollSerializer(polls).data 
#         return Response(data)

class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class PollDetail(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class ChoiceList(generics.ListCreateAPIView):
    # queryset = Choice.objects.all()
    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs['pk'])

        rich.print(
            Panel.fit(
                Text(
                    f"Choices: {', '.join([q.choice_text for q in queryset])}"
                ),
                style="blue"
            )
        )

        return queryset
    serializer_class = ChoiceSerializer
    


class CreateVote(generics.CreateAPIView):
    serializer_class = ChoiceSerializer

    def post(self, request, pk, choice_pk):
        voted_by = request.data.get("voted_by")
        date = {
            "choice": choice_pk,
            "poll": pk,
            "voted_by": voted_by
        }
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            # rich.print(
            #     Panel.fit(
            #         Text(
            #             seializer.data
            #         ),
            #         style="blue"
            #     )
            # )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = ()
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(
            username=username,
            password=password
        )
        if user:
            return Response(
                {
                    "token": user.auth_token.key
                }
            )
        else:
            return Response(
                {
                    "error": "Wrong Credentials"
                },
                status=status.HTTP_400_BAD_REQUEST
            )