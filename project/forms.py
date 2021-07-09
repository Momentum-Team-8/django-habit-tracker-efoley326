from django import forms
from .models import habitEntry


class habitForm(forms.ModelForm):
    class Meta:
        model = habitEntry
        fields = ('habit', 'amount',)
