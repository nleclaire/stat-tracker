from django import forms
from .models import Run

class DateInput(forms.DateInput):
    input_type = 'date'

class RunForm(forms.ModelForm):
    class Meta:
        model = Run
        fields = ['date', 'time', 'distance', 'average_speed', 'calories_burned', 'steps' ]
        # labels = {'text': ''}
        widgets = {
            'date': DateInput()
        }
