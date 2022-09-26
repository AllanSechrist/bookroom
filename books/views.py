from rest_framework import viewsets

from .permissions import IsOwnerOrReadOnly
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly,)
    # queryset = Book.objects.all()  # Change to user only books in future
    serializer_class = BookSerializer

    def get_queryset(self):
        return self.request.user.books.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

