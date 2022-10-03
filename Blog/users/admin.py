from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from typing import Any

from . import models 
from . import forms


class CUserAdmin(UserAdmin):
    add_form: Any = forms.CUserCreationFrom
    form = forms.CUserChangeForm
    model = models.CUser

admin.site.register(models.CUser, CUserAdmin)
