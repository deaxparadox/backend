from django.contrib import admin

from .models import Poll, Choice

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    pass 
    # list_display = ('question', 'pub_date')
    # list_filter = ('pub_date',)
    # search_fields = ('question',)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass 