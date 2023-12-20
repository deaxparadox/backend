from django.urls import path

from .views import task, heading

app_name = 'pms'

urlpatterns = [
    path("", heading.home_view, name="home"),
    path("d/<int:id>/", heading.detail_heading_view, name="detail_heading_view"),
    # path("t/d/<int:id>/", heading.detail_task_view, name="detail_task_view"),
    # path("h/<int:id>/", views.heading_edit, name="heading_edit"),
    path("c/h/", heading.create_heading_view, name="create_heading"),
    path("c/t/", task.create_task_view, name="create_task_view"),
    path("e/h/<int:id>/", heading.edit_heading_view, name="edit_heading_view"),
    path("e/t/<int:id>/", task.edit_task_view, name="edit_task_view"),
]
