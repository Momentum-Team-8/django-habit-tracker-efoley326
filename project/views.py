from django.shortcuts import render, redirect
from django.utils import timezone
import datetime
from django.http import HttpResponse
from .forms import habitForm

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return render(request, "project/template/tracker.html")

def habitForm(request):
    form = habitForm()
    return render(request, 'project/tracker.html', {'form': form})