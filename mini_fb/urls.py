from django.urls import path
from .views import (
    ShowAllProfilesView, ShowProfilePageView, CreateProfileView, 
    CreateStatusMessageView, UpdateProfileView, UpdateStatusMessageView, 
    DeleteStatusMessageView, CreateFriendView, ShowFriendSuggestionsView, ShowNewsFeedView
)

urlpatterns = [
    # Profile-related URLs
    path('profile/<int:pk>/', ShowProfilePageView.as_view(), name='show_profile'),
    path('profile/<int:pk>/create_status/', CreateStatusMessageView.as_view(), name='create_status'),

    # Create new profile URL
    path('create_profile/', CreateProfileView.as_view(), name='create_profile'),

    # Update existing profile URL
    path('profile/<int:pk>/update/', UpdateProfileView.as_view(), name='update_profile'),

    # Update and Delete status message URLs
    path('status/<int:pk>/update/', UpdateStatusMessageView.as_view(), name='update_status'),
    path('status/<int:pk>/delete/', DeleteStatusMessageView.as_view(), name='delete_status'),

    # Show all profiles (homepage)
    path('', ShowAllProfilesView.as_view(), name='show_all_profiles'),

    # Friend-related URLs
    path('profile/<int:pk>/add_friend/<int:other_pk>/', CreateFriendView.as_view(), name='add_friend'),
    path('profile/<int:pk>/friend_suggestions/', ShowFriendSuggestionsView.as_view(), name='friend_suggestions'),

    # News feed URL
    path('profile/<int:pk>/news_feed/', ShowNewsFeedView.as_view(), name='news_feed'),
]
