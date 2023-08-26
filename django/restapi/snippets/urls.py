from django.urls import path 
from snippets.views import regular as regular_views

app_name = "restapi"

urlpatterns = [
    path("snippets/", regular_views.snippet_list),
    path("snippets/<int:pk>/", regular_views.snippet_detail),
]
