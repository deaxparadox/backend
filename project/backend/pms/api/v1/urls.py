from django.urls import include, path




from . import views
from pms.api.v1.views import heading as heading


app_name = "pms_api_v1"

urlpatterns = [
    # mounted on the root
    # /api/v1/
    path(
        "", include(
            [
                # /api/v1/
                path("", heading.home_view, name="api_home_view"),
                
                # /api/v1/<int:id>/
                path("<int:id>/", heading.HeadingDetail.as_view(), name="api_single_heading_view"),
                
                # /api/v1/c/
                path("c/", heading.create_heading, name="api_create_heading_view"),
            ]
        )
    ),
    # mounted on path
    # /api/v1/
    path(
        "task/",
        include(
            [
                # /api/v1/task/
                path("", views.tasks_view, name="api_tasks_view"),
                
                # /api/v1/task/<int:id>/
                path("<int:id>/", views.get_single_task, name="api_single_tasks_view"),
            ]
        )
    ),
    
    
    
    
    
]