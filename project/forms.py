from django.forms import ModelForm
from .models import HabitEntry
from django import forms

class HabitForm(ModelForm):
    class Meta:
        model = HabitEntry
        fields = [
            'habit', 
            'amount',
            ]