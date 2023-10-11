from django.urls import path

from . import views

app_name = "api"

urlpatterns = [
    path("", views.person_all_view, name="index"),
    path("<int:id>/", views.person_one_view, name="one_person"),
]
