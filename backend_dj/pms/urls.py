from django.urls import path, include, re_path

from .views import task, heading

app_name = 'pms'

urlpatterns = [
    # heading views
    path(
        "", include([
            path("", heading.home_view, name="home"),
            path("<int:id>/detail/", heading.detail_heading_view, name="detail_heading_view"),
            path("<int:id>/update/", heading.update_heading_view, name="update_heading_view"),
            path("create/", heading.create_heading_view, name="create_heading_view"),
        ])
    ),
    
    # task view
    path(
        "task/",
        include(
            [
                path("<int:id>/", task.detail_task_view,  name="detail_task_view"),
                path("create/", task.create_task_view, name="create_task_view"),
                path("<int:id>/update/", task.update_task_view, name="update_task_view"),
            ]
        )
    )
]
