from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import HabitForm
from .models import HabitEntry

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect ('add_habit')
    else:
        return render(request, "base.html")
        

@login_required
def habit_list(request):
    habits = HabitEntry.objects.all()
    return render(request, "project/habit_list.html", {"habits": habits})

@login_required
def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.created_date = timezone.now()
            habit.save()
            return redirect(to='habit_list')
    else:
        form = HabitForm()
    return render (request, 'project/add_habit.html', {'form': form,})