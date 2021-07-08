from django.forms import ModelForm
from .models import Tracker


class enterHabit(ModelForm):

    class Meta:
        model = Tracker
        fields = [
            'habit',
            'date',
            'amount',
        ]