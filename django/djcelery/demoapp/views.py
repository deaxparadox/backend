from django.shortcuts import render
from django.http import JsonResponse

from celery.result import AsyncResult

from .tasks import add


def add_view(request):
    x = request.GET.get("x")
    y = request.GET.get("y")
    print(x, y)
    results = add.delay(int(x), int(y))
    return JsonResponse({
        "id": results.id
    })

def add_view_result(request, task_id):
    result = AsyncResult(task_id)
    return JsonResponse({
        "id": task_id,
        "status": result.status,
        "result": result.result
    })