from django.contrib import admin

from pms.models import (
    heading,
    task
)

class TaskInLine(admin.TabularInline): 
    model = task.Task

class HeadingAdmin(admin.ModelAdmin):
    ordering = ["created"]
    inlines = [
        TaskInLine
    ]

class TaskAdmin(admin.ModelAdmin):
    list_display = ["name", "created", "updated"]
    ordering = ["created"]
    raw_id_fields = ["heading"]
    
admin.site.register(heading.Heading, HeadingAdmin)
admin.site.register(task.Task, TaskAdmin)