from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from celery.result import AsyncResult

from .serializers import Add, AddSerializer
from ..tasks import add

@csrf_exempt
def add_view(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if not id:
            return JsonResponse(
                {
                    'message': "Invalid data!"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        task = AsyncResult(id)
        result = {
            "id": id,
            "status": task.status,
            "result": task.result
        }
        return JsonResponse(
            result,
            status=status.HTTP_200_OK
        )
        
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AddSerializer(data=data)
        if serializer.is_valid():
            values = Add(**serializer.validated_data)
            task = add.delay(values.x, values.y)
            return JsonResponse(
                {
                    "id": task.id
                }, status=201)
        return JsonResponse(serializer.errors, status=400)
