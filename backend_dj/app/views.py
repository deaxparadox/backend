from django.shortcuts import render, redirect
from django.urls import reverse


def root_page(request):
    # return render(
    #     request,
    #     "base.html"
    # )
    return redirect(reverse('app:dashboard'))

def dashboard_view(request):
    return render(
        request,
        "app/index.html"
    )