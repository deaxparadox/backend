from django.urls import path, include

from . import views

app_name = "chat"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
]
