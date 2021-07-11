from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms.models import ModelForm
from tracker.settings import TIME_ZONE


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class habitEntry(ModelForm):
        user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="entry")
        habit = models.CharField(max_length=255)
        amount = models.CharField(max_length=255, null=True, blank=True)

def __repr__(self):
    return {
        self.habit,
        self.amount,
        self.created_at,
        }

def __str__(self):
    return {self.habit}

