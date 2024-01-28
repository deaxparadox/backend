from django import forms

from pms.models.task import Task
from pms.models.heading import Heading

def get_heading_names() -> list[tuple]:
    heading_names = [('-1', "None")]
    for h in Heading.objects.all():
        heading_names.append((str(h.id), h.name))
    return heading_names

class TaskModelForm(forms.ModelForm):
    heading_names: list[tuple] = get_heading_names()

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
        required=False,
        help_text="Note describing your heading in less then 120 words"
    )
    select_heading = forms.ChoiceField(
        required=False,
        help_text="select a category heading",
        choices=heading_names
    )
    class Meta:
        model = Task
        exclude = ['heading']
        fields = "__all__"

    
    field_order = [
        # 'user',
        "select_heading",
        'name', 'description', 'note', 'start', 'end'
    ]