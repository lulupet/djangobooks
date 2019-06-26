from django.conf import settings
from django.db import models
from django.utils import timezone


class Book(models.Model):
    author = models.CharField(max_length=70)
    title = models.CharField(max_length=70)

    def create(self):
        self.save()

    def __str__(self):
        return self.title