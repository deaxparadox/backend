from django.contrib import admin

from .models import Question, Choice

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("choice_text", "votes",)

admin.site.register(Question)
admin.site.register(Choice, ChoiceAdmin)