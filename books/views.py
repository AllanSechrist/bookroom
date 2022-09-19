from rest_framework import viewsets

from .models import Book
from .permissions import IsOwnerOrReadOnly
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Book.objects.all()  # Change to user only books in future
    serializer_class = BookSerializer

