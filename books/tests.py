from django.test import TestCase

from .models import Book


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="test title",
            series="",
            publisher="test publisher",
            author="test author",
            isbn="1234567890123",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "test title")
        self.assertEqual(self.book.series, "")
        self.assertEqual(self.book.publisher, "test publisher")
        self.assertEqual(self.book.author, "test author")
        self.assertEqual(self.book.isbn, "1234567890123")
