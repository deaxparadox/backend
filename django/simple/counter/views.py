from django.shortcuts import render

def index(request):
    return render(request, "counter/index.html", {
        "name": "Counter",
        "default": 0,
    })