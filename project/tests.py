from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):
    def test_create_book(self):
        book = Book.objects.create(
            title="1984",
            author="George Orwell",
            genre="Dystopian",
            year_published=1949
        )
        self.assertEqual(book.title, "1984")
