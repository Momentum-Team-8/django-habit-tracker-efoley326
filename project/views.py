from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import HabitForm
from .models import HabitEntry

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return render(request, "base.html")

def habit_list(request):
    user = request.user
    habits = HabitEntry.objects.all()
    return render (request, "project/add_habit.html")

def add_habit(request):
    if request.method == 'GET':
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save()
            habit.save()
            return redirect(to=habit_list)
    return render(request, 'project/add_habit.html', {'form': form})