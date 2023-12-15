from django.shortcuts import render

def error_404(request):
    return render(request, "404.html")

def home_page(request):
    return render(
        request,
        "base.html"
    )