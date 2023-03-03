from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import (
    Paginator, EmptyPage, PageNotAnInteger
)

from .models import Post 


class PostListView(ListView):
    """
    Alternative post list view 
    """
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 1
    template_name = 'blog/post/list.html'