from django.urls import path 
from snippets.views import mixin_views

app_name = "snippet_mixin_views"

urlpatterns = [
    path("snippets/", mixin_views.SnippetList.as_view()),
    path("snippets/<int:pk>/", mixin_views.SnippetDetail.as_view()),
]
