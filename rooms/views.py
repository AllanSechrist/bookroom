from rest_framework import viewsets

from .permissions import IsOwnerOrReadOnly
from .serializers import RoomSerializer


class RoomViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly,)
    # queryset = Room.objects.all()  # user only in future
    serializer_class = RoomSerializer

    def get_queryset(self):
        return self.request.user.rooms.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

