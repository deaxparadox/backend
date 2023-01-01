from django.urls import path 

from . import views

app_name = "api"
urlpatterns = [
    path("", views.Todo.as_view(), name="api_list"),
]
