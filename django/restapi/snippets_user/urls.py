from django.urls import path 

from . import views

app_name = "snippets_user"

urlpatterns = [

    # users

    path("users/", views.UserList.as_view()),
    path("users/<int:pk>/", views.UserDetail.as_view()),
]
