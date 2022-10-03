from django import forms
from django.contrib.auth.forms import (
    UserChangeForm, UserCreationForm
)

from typing import Sequence

from . import models

class CUserCreationFrom(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = models.CUser
        fields: Sequence[str] = UserCreationForm.Meta.fields

class CUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = models.CUser
        fields: Sequence[str] = UserChangeForm.Meta.fields
