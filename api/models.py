from django.contrib.auth.models import AbstractUser
from django.db import models


class Note(models.Model):
    body = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
