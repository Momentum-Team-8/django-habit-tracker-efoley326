from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import habitForm

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return render(request, "project/template/tracker.html")

def habitForm(request):
    if request.method == 'POST':
        form = habitForm(request.POST)
        if form.is_valid():

            return HttpResponseRedirect ('/habit-list/')
    else: form = habitForm()
            
    return render (request, 'project/tracker.html', {'form': form})
