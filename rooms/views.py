from rest_framework import generics

from .models import Room
from .permissions import IsOwnerOrReadOnly
from .serializers import RoomSerializer


class RoomListView(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Room.objects.all()  # user only in future
    serializer_class = RoomSerializer


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Room.objects.all()  # user only in future
    serializer_class = RoomSerializer
