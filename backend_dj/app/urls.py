from django.urls import path, include, re_path

from . import views

app_name = "app"

urlpatterns = [
    path("", views.root_page, name="root"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
]
