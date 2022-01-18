from django import forms
from .models import Run, Split

class DateInput(forms.DateInput):
    input_type = 'date'

class RunForm(forms.ModelForm):
    class Meta:
        model = Run
        fields = ['date', 'time', 'distance', 'average_speed', 'calories_burned', 'steps' ]
        widgets = {
            'date': DateInput()
        }

class SplitForm(forms.ModelForm):
    class Meta:
        model = Split
        fields = ['date', 'time', 'length', 'run']
        # labels = {'time': '00:'}
        widgets = {
            'time': forms.TimeField()
        }
