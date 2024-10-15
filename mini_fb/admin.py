from django.contrib import admin
from .models import Profile, StatusMessage

# Ensure you're not registering the same model twice
admin.site.register(Profile)
admin.site.register(StatusMessage)

