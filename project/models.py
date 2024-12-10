from django.db import models
from django.contrib.auth.models import AbstractUser

# User Model
class User(AbstractUser):  # Extend the default User model for customization
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


# Category Model
class Category(models.Model):  # Represents book categories
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# Book Model
class Book(models.Model):  # Represents books in the library
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    year_published = models.PositiveIntegerField()
    is_borrowed = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='books'
    )

    def __str__(self):
        return self.title


# Borrower Model
class Borrower(models.Model):  # Tracks borrowed books
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrowers')
    borrower_name = models.CharField(max_length=255)
    borrow_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return f"{self.borrower_name} - {self.book.title}"


# Reminder Model
class Reminder(models.Model):  # Represents reminders for books
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reminders')
    reminder_date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reminder for {self.book.title} on {self.reminder_date}"


# Review Model
class Review(models.Model):  # Represents book reviews
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(default=1)  # Rating scale: 1-5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s review of {self.book.title} ({self.rating}/5)"
