from django.urls import path, include, re_path

from . import views

app_name = "python"

urlpatterns = [
    path("", views.home, name="home")
]
