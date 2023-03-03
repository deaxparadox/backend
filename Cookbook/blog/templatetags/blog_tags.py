from django import template
from ..models import Blog

register = template.Library()


@register.simple_tag 
def total_posts():
    return 

@register.inclusion_tag("blog/include/latest_blogs.html")
def show_latest_blogs():
    latest_blogs: list = Blog.objects.all()
    # print(latest_blogs)
    return {
        "latest_blogs": latest_blogs
    }

@register.inclusion_tag("blog/include/recommended_blogs.html")
def show_recommended_blogs():
    latest_blogs: list = Blog.objects.all()
    # print(latest_blogs)
    return {
        "latest_blogs": latest_blogs
    }