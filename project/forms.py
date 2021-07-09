from django.forms import ModelForm
from .models import habitEntry


class enterHabit(ModelForm):
    class Meta:
        model = habitEntry
        fields = [
            'habit',
            'amount',
        ]
