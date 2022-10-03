from django.urls import path 

from . import views
urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path('<int:pk>/profile/', views.ProfileUpdate.as_view(), name="user_profile")
]
