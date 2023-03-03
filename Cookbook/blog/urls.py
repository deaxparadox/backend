from django.urls import path, include, re_path
from rest_framework.authtoken import views

from .views import (
    home_view, blog_detail, blog_create
)
from .apiview import (
    BlogsAPIView, UserCreateAPIView
)

app_name = "blog"

urlpatterns = [
    path("v1/api/", BlogsAPIView.as_view(), name="blogs"),
    path("v1/api/login/", views.obtain_auth_token, name="api_login"),
    path("v1/api/create/", UserCreateAPIView.as_view() , name="api_create_user"),
    # 
    path("v1/", home_view, name="home"),
    path("v1/create/", blog_create, name="create"),
    path("v1/<slug:title>/", blog_detail, name="detail"),
    # 
    
]