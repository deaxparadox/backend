from django.urls import path, include, re_path

from . import views

app_name = "maths"

urlpatterns = [
    path("submit/", views.submit, name="submit"),
    path("result/<str:task_id>/", views.result, name="result"),
]
