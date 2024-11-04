from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    ShowAllProfilesView, ShowProfilePageView, CreateProfileView, 
    CreateStatusMessageView, UpdateProfileView, UpdateStatusMessageView, 
    DeleteStatusMessageView, CreateFriendView, ShowFriendSuggestionsView, ShowNewsFeedView,
    AboutView, ContactView  # Assuming these views exist
)

urlpatterns = [
    # Profile-related URLs
    path('profile/', ShowProfilePageView.as_view(), name='show_profile'),  # For logged-in user's profile
    path('profile/view/<int:pk>/', ShowProfilePageView.as_view(), name='view_profile'),  # For viewing any profile by pk

    # Status message URLs
    path('status/create_status/', CreateStatusMessageView.as_view(), name='create_status'),
    path('status/<int:pk>/update/', UpdateStatusMessageView.as_view(), name='update_status'),
    path('status/<int:pk>/delete/', DeleteStatusMessageView.as_view(), name='delete_status'),

    # Create new profile URL
    path('create_profile/', CreateProfileView.as_view(), name='create_profile'),

    # Update existing profile URL
    path('profile/update/', UpdateProfileView.as_view(), name='update_profile'),

    # Show all profiles (homepage)
    path('', ShowAllProfilesView.as_view(), name='show_all_profiles'),

    # Friend-related URLs
    path('profile/add_friend/<int:other_pk>/', CreateFriendView.as_view(), name='add_friend'),
    path('profile/friend_suggestions/', ShowFriendSuggestionsView.as_view(), name='friend_suggestions'),

    # News feed URL
    path('profile/news_feed/', ShowNewsFeedView.as_view(), name='news_feed'),

    # About and Contact URLs
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='mini_fb/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='mini_fb/logged_out.html'), name='logout'),
]
