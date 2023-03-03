from django.shortcuts import render

from rest_framework import generics

from .models import Blog
from .serializers import BlogSerializer
from .forms import BlogForm


def home_view(request):
    blogs: Blog() = Blog.objects.all()
    return render(
        request,
        "blog/index.html",
        {
            "blogs": blogs
        }
    )

def blog_detail(request, title):
    blog = Blog.objects.get(slug=title)
    return render(
        request,
        "blog/detail.html",
        {
            "blog": blog
        }
    )

def blog_create(request):
    if request.method == "POST":
        blog_form = BlogForm(request.POST)
        if blog_form.is_valid():
            blog = blog_form.save(commit=False)
            # blog.author = request.user
            blog.save()
            return render(
                request,
                "blog/detail.html",
                {
                    "blog": blog
                }
            )
    else:
        blog_form = BlogForm()
    return render(
        request,
        "blog/create.html",
        {
            "blog_form": blog_form
        }
    )

