from django.contrib import admin
from typing import Sequence

from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display: Sequence[str] = ('title', 'content', "date_time")
    list_filter: Sequence[str] = ('date_time',)
    search_fields: Sequence[str] = ('title', 'content')