from django.contrib import admin
from .models import Profile, StatusMessage, Image, Friend  # Import Friend model

# Register your models here
admin.site.register(Profile)
admin.site.register(StatusMessage)
admin.site.register(Image)
admin.site.register(Friend)  # Register the Friend model to the admin site
