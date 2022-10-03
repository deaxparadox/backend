from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from typing import *

from . import models 

class BlogCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Blog
    template_name: str = "blog/blog_create/blog_create.html"
    fields = ["title", "body"]
    success_url = "/blog/"
    login_url: Any = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogListView(LoginRequiredMixin, generic.ListView):
    template_name: str = "blog/blog_list/blog_list.html"
    model = models.Blog
    context_object_name: str = "blog_list"
    login_url: Any = "login"

    # def get_queryset(self):
    #     return models.Blog.objects.filter(author=self.request.user)


class BlogListUserView(BlogListView):
    template_name: str = "blog/blog_list_user/blog_list_user.html"
    model = models.Blog
    context_object_name: str = "blog_list_user"
    login_url: Any = "login"

    def get_queryset(self):
        return models.Blog.objects.filter(author=self.request.user)




class BlogDetailView(LoginRequiredMixin,generic.DetailView):
    template_name: str = "blog/blog_detail/blog_detail.html"
    model = models.Blog
    context_object_name: str = "blog_detail"
    login_url: Any = "login"

class BlogUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.Blog
    template_name: str = "blog/blog_update/blog_update.html"
    fields = ['title', 'body']
    success_url = "/blog/"
    login_url: Any = "login"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

class BlogDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = models.Blog
    template_name: str = "blog/blog_delete/blog_delete.html"
    success_url: Optional[str] = "/blog/"
    context_object_name: str = "blog_delete"
    login_url: Any = "login"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    