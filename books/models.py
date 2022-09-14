from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=250)
    series = models.CharField(max_length=250, blank=True)
    publisher = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title
