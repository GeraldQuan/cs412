from django.urls import path
from . import views  # This is correct, as it imports from the quotes app

urlpatterns = [
    path('', views.quote, name='quote'),
    path('quote/', views.quote, name='quote'),
    path('show_all/', views.show_all, name='show_all'),
    path('about/', views.about, name='about'),
]
