from django.urls import path, include

from .views import add

app_name = "demoapp"

urlpatterns = [
    path("add/", add, name="add")
]
