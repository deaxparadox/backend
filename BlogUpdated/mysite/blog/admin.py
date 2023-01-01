from django.contrib import admin
from typing import Sequence, Mapping, Union, Callable, Any, Optional

from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display: Sequence[Union[str, Callable[[], Any]]] = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    prepopulated_fields: Mapping[str, Sequence[str]] = {"slug": ('title',)}
    
    search_fields: Sequence[str] = ['title', 'body']
    raw_id_fields: Sequence[str] = ['author']
    date_hierarchy: Optional[str] = 'publish'
    ordering: Sequence[str] = ['status', 'publish']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display: Sequence[Union[str, Callable[[], Any]]] = ['name', 'email', 'post', 'created', 'active']
    list_filter: Sequence = ['active', 'created', 'updated']
    search_fields: Sequence[str] = ['name', 'email', 'body']