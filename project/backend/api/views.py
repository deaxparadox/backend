from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET"])
def home_api(request):
    return Response(
        {
            "message": "This is the REST API home."
        },
        status=status.HTTP_200_OK
    )