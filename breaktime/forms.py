from django import forms
from .models import Break

class BreakForm(forms.ModelForm):
    class Meta:
        model = Break
        fields = ["start_time", "end_time", "activity", "place", "recreation"]
        widgets = {
            "start_time": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "end_time": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }