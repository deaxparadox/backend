from django.urls import path, re_path

from . import views

app_name = "app"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("app/", views.AppsView.as_view(), name="app"),
]
