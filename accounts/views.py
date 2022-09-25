from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import CustomUser
from .serializers import UserSerializer
from rooms.serializers import RoomSerializer
from .permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    # @action(detail=True)
    # def get_rooms(self, request, pk=None):
    #     user_rooms = self.get_object().room_set
    #     serializer = RoomSerializer(data=user_rooms)
    #     if serializer.is_valid():

    #         return Response({"Rooms": user_rooms})

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
