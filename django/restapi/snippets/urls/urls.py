from django.urls import path 
from snippets.views import (
    regular as regular_views,
    format_suffix,
    wrappers,
    class_views,
    mixin_views,
    generic_views
)

app_name = "restapi"

urlpatterns = [

    # regular views

    path("", regular_views.snippet_list),
    path("<int:pk>/", regular_views.snippet_detail),
    
] + [

    # regular view with format suffix
    
    path(
        "format_suffix/", 
        format_suffix.snippet_list, 
        name="snippet_format_suffix"
    ),
    path(
        "format_suffix/<int:pk>/", 
        format_suffix.snippet_detail, 
        name="snippet_format_suffix_detail"
    ),

] + [

    # class based views

    path(
        "class_view/", 
        class_views.SnippetList.as_view(), 
        name="snippet_class_view"
    ),
    path(
        "class_view/<int:pk>/", 
        class_views.SnippetDetail.as_view(), 
        name="snippet_class_view_detail"
    ),
] + [

    # class based mixin views

    path(
        "mixin_view/", 
        mixin_views.SnippetList.as_view(), 
        name="snippet_mixin_view"
    ),
    path(
        "mixin_view/<int:pk>/", 
        mixin_views.SnippetDetail.as_view(), 
        name="snippet_mixin_view_detail"
    ),
] + [

    # class based generic views

    path(
        "generic_view/", 
        generic_views.SnippetList.as_view(), 
        name="snippet_generic_view"
    ),
    path(
        "generic_view/<int:pk>/", 
        generic_views.SnippetDetail.as_view(), 
        name="snippet_generic_view_detail"
    ),
] 