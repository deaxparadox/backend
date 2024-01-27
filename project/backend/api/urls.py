from django.urls import path, include, re_path

from . import views

app_name = "app_api"

urlpatterns = [
    path("", views.home_api, name="home"),
]
