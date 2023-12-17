from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from ..models.headings import Heading

# class HeadingDateInput(forms.TextInput):
#     input_type = 'date'

class HeadingModelForm(forms.ModelForm):
    start = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        required=False,
        label='Start',
        help_text="specify the start (or initial) date"
    )
    end = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        required=False,
        label='End',
        help_text="specify the end (or final) date"
    )
    class Meta:
        model = Heading
        fields = "__all__"
        # widgets = {
        #     "end": forms.DateInput(attrs={"type": "date"})
        # }