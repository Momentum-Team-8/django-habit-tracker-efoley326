from django.contrib import admin
from .models import User, HabitEntry, HabitList

# Register your models here.
admin.site.register(User)
admin.site.register(HabitEntry)
admin.site.register(HabitList)