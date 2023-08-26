from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import class_views

app_name = "snippet_class_views"

urlpatterns = [
    path("snippets/", class_views.SnippetList.as_view()),
    path("snippets/<int:pk>/", class_views.SnippetDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)