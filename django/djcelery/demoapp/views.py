from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from celery.result import AsyncResult

from .tasks import add

def home(request):
    return render(
        request,
        "demoapp/index.html"
    )



@csrf_exempt
def add_view(request):
    x = request.POST.get("x")
    y = request.POST.get("y")
    print(x, y)
    results = add.delay(int(x), int(y))
    return JsonResponse({
        "id": results.id
    })


@csrf_exempt
def add_view_result(request, task_id):
    result = AsyncResult(task_id)
    return JsonResponse({
        "id": task_id,
        "status": result.status,
        "result": result.result
    })