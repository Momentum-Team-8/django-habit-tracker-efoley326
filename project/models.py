from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class habitEntry(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="entry")
    habit = models.CharField(max_length=255)
    amount = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

