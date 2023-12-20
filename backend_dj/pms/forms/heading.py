from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from pms.models.heading import Heading

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
    note = forms.CharField(
        # widget=forms.CharField(attrs={'type': 'text'}),
        required=False,
        help_text="Note describing your heading in less then 120 words"
    )
    class Meta:
        model = Heading
        fields = "__all__"
        # widgets = {
        #     "end": forms.DateInput(attrs={"type": "date"})
        # }
        
    field_order = ['user', 'name', 'description', 'note', 'start', 'end']