from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from celery.result import AsyncResult

@api_view(["GET"])
def home_api(request):
    return Response(
        {
            "message": "This is the REST API home."
        },
        status=status.HTTP_200_OK
    )



@api_view(["GET"])
def result(request, task_id):
    match request.method:
        case "GET":
            task_result = AsyncResult(task_id)
            result = {
                "task_id": task_id,
                "status": task_result.status,
                "result": task_result.result
            }
            return Response(result, status=status.HTTP_200_OK)
        case _: 
            return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    