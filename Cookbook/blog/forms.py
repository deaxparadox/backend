from django import forms
from typing import Sequence

from . import models

class BlogForm(forms.ModelForm):
    class Meta:
        model: models.Blog = models.Blog
        fields: Sequence[str] = ('title', 'content')
   