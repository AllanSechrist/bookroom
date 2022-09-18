from django.conf import settings
from django.db import models

from books.models import Book


class Room(models.Model):
    name = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=300)
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, related_name="books")

    def __str__(self):
        return self.name