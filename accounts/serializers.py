from rest_framework import serializers

from .models import CustomUser
from rooms.serializers import RoomSerializer
from books.serializers import BookSerializer
from rooms.models import Room
from books.models import Book


class UserSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True)
    books = BookSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "rooms",
            "books",
        )

    #