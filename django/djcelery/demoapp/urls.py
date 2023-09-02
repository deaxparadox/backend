from django.urls import path, include

from . import views

app_name = "demoapp"

urlpatterns = [
    path("add/", views.add_view, name="add"),
    path("add/<str:task_id>/", views.add_view_result, name="add_result"),
]
