from django.urls import path

from .views import ListView

app_name = "appapi"

urlpatterns = [
    path("", ListView.as_view(), name="index")
]
