from django.urls import path 

from ..views_extend import views_projects

urlpatterns = [
    path("project/counter/", views_projects.ProjectCounterView.as_view(), name="programming_project_counter"),
]
