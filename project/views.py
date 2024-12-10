from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Book, Borrower, Reminder, Category, Review
from .forms import BookForm, BorrowerForm, ReminderForm, ReviewForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Home View
def home(request):
    """Render the home page."""
    return render(request, "project/home.html")

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'project/signup.html'
    success_url = reverse_lazy('login')  # Redirect to login after successful signup


# Book Views
class BookListView(LoginRequiredMixin, ListView):
    """View to list all books."""
    model = Book
    template_name = "project/book_list.html"
    context_object_name = "books"


class BookDetailView(LoginRequiredMixin, DetailView):
    """View to show details of a specific book."""
    model = Book
    template_name = "project/book_detail.html"
    context_object_name = "book"


class BookCreateView(LoginRequiredMixin, CreateView):
    """View to create a new book."""
    model = Book
    form_class = BookForm
    template_name = "project/book_form.html"
    success_url = reverse_lazy("book-list")


class BookUpdateView(LoginRequiredMixin, UpdateView):
    """View to update an existing book."""
    model = Book
    form_class = BookForm
    template_name = "project/book_form.html"
    success_url = reverse_lazy("book-list")


class BookDeleteView(LoginRequiredMixin, DeleteView):
    """View to delete an existing book."""
    model = Book
    template_name = "project/book_confirm_delete.html"
    success_url = reverse_lazy("book-list")


# Borrower Views
class BorrowerListView(LoginRequiredMixin, ListView):
    """View to list all borrowers."""
    model = Borrower
    template_name = "project/borrower_list.html"
    context_object_name = "borrowers"


class BorrowerCreateView(LoginRequiredMixin, CreateView):
    """View to create a new borrower."""
    model = Borrower
    form_class = BorrowerForm
    template_name = "project/borrower_form.html"
    success_url = reverse_lazy("borrower-list")


# Reminder Views
class ReminderListView(LoginRequiredMixin, ListView):
    """View to list all reminders."""
    model = Reminder
    template_name = "project/reminder_list.html"
    context_object_name = "reminders"


class ReminderCreateView(LoginRequiredMixin, CreateView):
    """View to create a new reminder."""
    model = Reminder
    form_class = ReminderForm
    template_name = "project/reminder_form.html"
    success_url = reverse_lazy("reminder-list")


# Category Views
class CategoryListView(LoginRequiredMixin, ListView):
    """View to list all categories."""
    model = Category
    template_name = "project/category_list.html"
    context_object_name = "categories"


class CategoryCreateView(LoginRequiredMixin, CreateView):
    """View to create a new category."""
    model = Category
    fields = ['name', 'description']
    template_name = "project/category_form.html"
    success_url = reverse_lazy("category-list")


# Review Views
class ReviewCreateView(LoginRequiredMixin, CreateView):
    """View to create a new review for a book."""
    model = Review
    form_class = ReviewForm
    template_name = "project/review_form.html"

    def form_valid(self, form):
        """Attach the book to the review and optionally the current user."""
        book_id = self.kwargs.get('book_id')
        book = get_object_or_404(Book, id=book_id)
        form.instance.book = book

        # Optionally attach the current user to the review
        form.instance.user = self.request.user if self.request.user.is_authenticated else None
        return super().form_valid(form)

    def get_success_url(self):
        """Redirect to the book detail page after review creation."""
        return reverse_lazy('book-detail', kwargs={'pk': self.kwargs.get('book_id')})
