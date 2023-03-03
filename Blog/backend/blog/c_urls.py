from django.urls import path

from . import c_views
from . import views 
from .api import apiview
app_name = "blog"

urlpatterns = [
    path("", c_views.PostListView.as_view(), name="post_list"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/", 
        views.post_detail, 
        name="post_detail"
    ),

    # API
    path("api/", apiview.BlogListView.as_view(), name="api_post_list"),
]