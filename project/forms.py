from django.forms import ModelForm
from .models import HabitEntry


class HabitForm(ModelForm):
    class Meta:
        model = HabitEntry
        fields = [
            'habit', 
            'amount',
        ]