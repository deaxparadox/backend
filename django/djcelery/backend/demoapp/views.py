from django.shortcuts import render
from django.views.decorators.http import require_GET
from rest_framework.parsers import JSONParser
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .api.serializers import AddSerializer

from celery.result import AsyncResult

from .tasks import add

def home(request):
    return render(
        request,
        "demoapp/index.html"
    )



@csrf_exempt
@require_GET
def common_add_view(request):
    task_id = request.GET.get("id", None)
    x = request.GET.get("x", None)
    y = request.GET.get("y", None)

    print(task_id, x, y)

    if not task_id:



        if not x or not y:
            return JsonResponse({"message": "Invalid Values!"})
        
        results = add.delay(int(x), int(y))
        return JsonResponse({
            "id": results.id
        })

    else:
        print(task_id)

        if not task_id:
            return HttpResponse("No task id found.")
        
        # return HttpResponse("Welcome to Add.")
        result = AsyncResult(task_id)
        return JsonResponse({
            "id": task_id,
            "status": result.status,
            "result": result.result
        })

    return JsonResponse({"message": "Welcome to Add."})


@csrf_exempt
def post_add_view(request, task_id = None):
    print(f"post_add_view: {request.method}")
    match request.method:
        case "POST":
            x = request.POST.get("x", None)
            y = request.POST.get("y", None)

            print(f"post_add_view: {x}, {y}")
        

            if not x or not y:
                return JsonResponse({"message": "Invalid Values!"})
            
            results = add.delay(int(x), int(y))
            return JsonResponse({
                "id": results.id
            })
        case _:
            if not task_id:
                task_id = request.GET.get("id")
            
            print(f"post_add_view: {task_id}")

            if not task_id:
                return JsonResponse({"message": "No task id found."})
            
            # return HttpResponse("Welcome to Add.")
            result = AsyncResult(task_id)
            return JsonResponse({
                "id": task_id,
                "status": result.status,
                "result": result.result
            })

@csrf_exempt
def result(request, task_id):
    result = AsyncResult(task_id)
    return JsonResponse({
        "id": task_id,
        "status": result.status,
        "result": result.result
    })