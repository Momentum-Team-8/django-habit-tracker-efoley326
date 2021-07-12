from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import habitForm
from .models import habitEntry

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return render(request, "project/template/tracker.html")

def habitForm(request):
    form = habitForm()
    if form.is_valid():
        return render (habitEntry)
    else: form = habitForm()
            
    return render (request, 'project/template/tracker.html', {'form': form})
