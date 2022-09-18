from rest_framework import generics

from .models import Book
from .permissions import IsOwnerOrReadOnly
from .serializers import BookSerializer


class BookListView(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Book.objects.all()  # Change to user only books in future
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Book.objects.all()  # Change to user only books in future
    serializer_class = BookSerializer
