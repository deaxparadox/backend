from django import forms

from . import models

class Todo(forms.ModelForm):
    class Meta:
        model = models.TodoForm
        fields = "__all__"