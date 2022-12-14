from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "series",
            "publisher",
            "author",
            "isbn",
            "user",
        )
        