from django.shortcuts import render
from django.http import JsonResponse


from .tasks import add


def add(request):
    x = request.GET.get("x")
    y = request.GET.get("y")
    results = add.delay(int(x), int(y))
    return JsonResponse({
        "id": results.id
    })