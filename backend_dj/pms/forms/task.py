from django import forms

from pms.models.task import Task
from pms.models.heading import Heading

class TaskModelForm(forms.ModelForm):
    heading_names = [
        (str(h.id), h.name) for h in Heading.objects.all()
    ]
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