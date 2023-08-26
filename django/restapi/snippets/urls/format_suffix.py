from django.urls import path 
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import format_suffix

app_name = "snippet_format_suffix"

urlpatterns = [
    path("snippets/", format_suffix.snippet_list),
    path("snippets/<int:pk>/", format_suffix.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)