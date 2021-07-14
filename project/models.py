from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone



class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class HabitEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    habit = models.CharField(max_length=255)
    amount = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return {self.habit}
class HabitList(models.Model):
    name = models.CharField(max_length=256)
    
    def __str__ (self):
        return self.name


