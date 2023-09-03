from django.urls import path, include

from . import views
from .api import views as api_views

app_name = "demoapp"

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.common_add_view, name="add"),
    path("post-add/", views.post_add_view, name="post_add"),
    path("post-add/<str:task_id>/", views.post_add_view, name="post_add_result"),
    path("add/api/", api_views.add_view, name="add_view_api"),
    path("result/<str:task_id>/", views.result, name="result"),
]
