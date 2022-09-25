from rest_framework import serializers

from .models import CustomUser
from rooms.models import Room


class UserSerializer(serializers.ModelSerializer):
    rooms = serializers.PrimaryKeyRelatedField(many=True, queryset=Room.objects.all())

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "rooms",
        )

    #