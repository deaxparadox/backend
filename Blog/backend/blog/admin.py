from django.contrib import admin
import typing 

from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title", "slug", "author", "publish", "status"
    ]
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {"slug": ("title", )}
    raw_id_fields = ["author"]
    date_hierarchy = "publish"
    ordering = ['status', 'publish']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_fitler = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']