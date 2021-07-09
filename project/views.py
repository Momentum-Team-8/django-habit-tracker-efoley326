from django.shortcuts import render, redirect
from django.utils import timezone
import datetime
from .forms import enterHabit
from .models import habitEntry

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect(to="enterHabit")

    return render(request, "project/index.html")

def habitEntry(request):
    if request.method =="POST":
        form = enterHabit(data=request.POST)
        
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
    return render (request, "templates/tracker.html", {"form": form},
        )