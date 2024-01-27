from django.urls import path, include, re_path

from . import views

app_name = "app"

urlpatterns = [
    path("", views.home, name="home")
]
