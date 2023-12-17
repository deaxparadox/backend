from django import forms

from ..models.tasks import Task

class TaskModelForm(forms.ModelForm):
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
        model = Task
        fields = "__all__"