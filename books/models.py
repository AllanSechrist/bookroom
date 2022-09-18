from django.db import models
from django.conf import settings


class Book(models.Model):
    title = models.CharField(max_length=250)
    series = models.CharField(max_length=250, blank=True)
    publisher = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    isbn = models.CharField(max_length=13)
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
