from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Room
from books.models import Book


class RoomTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@test.com",
            password="password123",
        )

        cls.book = Book.objects.create(
            title="test title",
            series="",
            publisher="test publisher",
            author="test author",
            isbn="1234567890123",
            user=cls.user,
        )

        cls.booktwo = Book.objects.create(
            title="test title 2",
            series="",
            publisher="test publisher 2",
            author="test author",
            isbn="3210987654321",
            user=cls.user,
        )

        cls.room = Room.objects.create(
            name="test room",
            subtitle="My top 10 tests!",
            user=cls.user,
        )
        cls.room_empty = Room.objects.create(
            name="empty room",
            subtitle="Test empty",
            user=cls.user,
        )

        cls.room.books.add(cls.book)
        cls.room.books.add(cls.booktwo)

    def test_room_model(self):
        self.assertEqual(self.room.user.username, "testuser")
        self.assertEqual(self.room.name, "test room")
        self.assertEqual(self.room.subtitle, "My top 10 tests!")
        self.assertEqual(self.book.user.username, "testuser")
        self.assertEqual(self.room.books.count(), 2)
        self.assertEqual(self.room_empty.books.count(), 0)
        self.assertEqual(self.room.user.room_set.count(), 2)
