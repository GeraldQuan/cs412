from django.urls import path
from . import views  # This is correct, as it imports from the quotes app
from django.urls import path
from .views import quotes, show_all

urlpatterns = [
    path('', quotes, name='quote_of_the_day'),  # Explicit route for quotes app
    path('show/', show_all, name='show_all_quotes'),  # Additional routes
]
