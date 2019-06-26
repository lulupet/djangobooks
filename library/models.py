from django.conf import settings
from django.db import models
from django.utils import timezone


class Book(models.Model):
    author = models.TextField()
    title = models.TextField()

    def create(self):
        self.save()

    def __str__(self):
        return self.title