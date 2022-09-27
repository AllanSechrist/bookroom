from django.conf import settings
from django.db import models

from books.models import Book


class Room(models.Model):
    name = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=300)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="rooms", on_delete=models.CASCADE, default=1)
    books = models.ManyToManyField(Book, blank=True, related_name="books")

    def __str__(self):
        return self.name