from django.contrib import admin
from .models import User, Book, Borrower, Reminder, Category, Review

# Customize User Admin
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    ordering = ('username',)


# Customize Book Admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'year_published', 'is_borrowed', 'category')
    list_filter = ('genre', 'is_borrowed', 'category')
    search_fields = ('title', 'author')
    ordering = ('title',)


# Customize Borrower Admin
@admin.register(Borrower)
class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('borrower_name', 'book', 'borrow_date', 'return_date')
    list_filter = ('borrow_date', 'return_date')
    search_fields = ('borrower_name', 'book__title')
    ordering = ('borrow_date',)


# Customize Reminder Admin
@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('book', 'reminder_date', 'notes')
    list_filter = ('reminder_date',)
    search_fields = ('book__title', 'notes')
    ordering = ('reminder_date',)


# Customize Category Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)


# Customize Review Admin
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('book__title', 'user__username')
    ordering = ('created_at',)
