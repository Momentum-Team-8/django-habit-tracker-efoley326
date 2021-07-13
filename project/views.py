from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import HabitForm
from .models import HabitEntry

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return render(request, "project/add_habit.html")

def habit_list(request):
    user = request.user
    habits = HabitEntry.objects.all()
    return render (request, "add_habit.html")

def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(data=request.POST)
        if form.is_valid():
            return render (HabitEntry)
    else: form = HabitForm()
    return render (request, 'habit_list.html', {'form': form})