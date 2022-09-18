from rest_framework import generics

from .models import Room
from .serializers import RoomSerializer


class RoomListView(generics.ListCreateAPIView):
    queryset = Room.objects.all()  # user only in future
    serializer_class = RoomSerializer


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()  # user only in future
    serializer_class = RoomSerializer
