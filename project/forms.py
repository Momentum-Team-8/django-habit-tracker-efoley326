from django.forms import ModelForm
from .models import habitEntry


class habitForm(ModelForm):
    class Meta:
        model = habitEntry
        fields = [
            'user',
            'habit', 
            'amount',
        ]