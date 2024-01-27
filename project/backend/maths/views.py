from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http  import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from celery.result import AsyncResult


from .tasks import task_sum

# @api_view(["POST"])
@csrf_exempt
def submit(request):
    print(f"\n{request.POST}\n")
    a = request.POST.get("a")
    b = request.POST.get("b")
    
    if not a or not b:
        return JsonResponse({"error": "Invalid Data or Type"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    print(a, b)

    task_id = task_sum.delay(int(a), int(b))
    return JsonResponse({"task_id": task_id.id}, status=status.HTTP_202_ACCEPTED)

# @api_view(["GET"])
# def result(request, task_id):
#     match request.method:
#         case "GET":
#             task_result = AsyncResult(task_id)
#             result = {
#                 "task_id": task_id,
#                 "status": task_result.status,
#                 "result": task_result.result
#             }
#             return Response(result, status=status.HTTP_200_OK)
#         case _: 
#             return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    