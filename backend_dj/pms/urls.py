from django.urls import path

from . import views

app_name = 'pms'

urlpatterns = [
    path("", views.home_view, name="home"),
    # path("h/<int:id>/", views.heading_edit, name="heading_edit"),
    path("c/h/", views.create_heading_view, name="create_heading_view"),
    path("c/t/", views.create_task_view, name="create_task_view"),
    path("e/h/<int:id>/", views.edit_heading_view, name="edit_heading_view"),
    path("e/t/<int:id>/", views.edit_task_view, name="edit_task_view"),
]
