from rest_framework import generics

from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()  # Change to user only books in future
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestoryAPIView):
    queryset = Book.objects.all()  # Change to user only books in future
    serializer_class = BookSerializer
