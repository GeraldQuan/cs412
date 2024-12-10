from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Home Page
    path('', views.home, name='home'),

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='project/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),  # Signup URL

    # Book-related URLs
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/add/', views.BookCreateView.as_view(), name='book-add'),  # Ensure consistency
    path('books/<int:book_id>/reviews/add/', views.ReviewCreateView.as_view(), name='review-add'),
    path('books/<int:pk>/edit/', views.BookUpdateView.as_view(), name='book-edit'),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),

    


    # Category-related URLs
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/add/', views.CategoryCreateView.as_view(), name='category-add'),  # Add Category creation URL

    # Borrower-related URLs
    path('borrowers/', views.BorrowerListView.as_view(), name='borrower-list'),
    path('borrowers/add/', views.BorrowerCreateView.as_view(), name='borrower-create'),  # Use a single name here
    path('borrowers/add/', views.BorrowerCreateView.as_view(), name='borrower-add'),  # Ensure consistency

    # Reminder-related URLs
    path('reminders/', views.ReminderListView.as_view(), name='reminder-list'),
    path('reminders/add/', views.ReminderCreateView.as_view(), name='reminder-create'),  # Use a single name here
    path('reminders/add/', views.ReminderCreateView.as_view(), name='reminder-add'),

    # Review-related URLs
    path('books/<int:book_id>/reviews/add/', views.ReviewCreateView.as_view(), name='review-add'),
]

