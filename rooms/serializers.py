from rest_framework import serializers

from .models import Room
from books.serializers import BookSerializer


class RoomSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Room
        fields = (
            "id",
            "name",
            "subtitle",
            "user",
            "books",
        )
