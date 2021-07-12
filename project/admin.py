from django.contrib import admin
from .models import User, habitEntry

# Register your models here.
admin.site.register(User)
admin.site.register(habitEntry)