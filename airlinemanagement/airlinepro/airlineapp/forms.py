# flights/forms.py
from django import forms
from .models import Flight

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['flight_id', 'dep_airport', 'dep_date', 'dep_time', 'arr_airport', 'arr_date', 'arr_time']
        widgets = {
            'dep_date': forms.DateInput(attrs={'type': 'date'}),
            'arr_date': forms.DateInput(attrs={'type': 'date'}),
            'dep_time': forms.TimeInput(attrs={'type': 'time'}),
            'arr_time': forms.TimeInput(attrs={'type': 'time'}),
        }
