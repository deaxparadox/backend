from django.urls import path 
from snippets.views import generic_views

app_name = "snippet_generic_views"

urlpatterns = [
    path("snippets/", generic_views.SnippetList.as_view()),
    path("snippets/<int:pk>/", generic_views.SnippetDetail.as_view()),
]
