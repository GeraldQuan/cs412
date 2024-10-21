from django.db import models
from django.utils import timezone
from django.urls import reverse

class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    profile_image_url = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_status_messages(self):
        # Return all status messages related to this profile, ordered by timestamp
        return self.statusmessage_set.all().order_by('-timestamp')

    def get_absolute_url(self):
        # Returns the URL to the profile detail page
        return reverse('show_profile', kwargs={'pk': self.pk})


class StatusMessage(models.Model):
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)  # ForeignKey relationship to Profile

    def get_images(self):
        # Return all images related to this status message
        return self.image_set.all()

    def __str__(self):
        # String representation for the admin and other use cases
        return f"{self.profile.first_name} {self.profile.last_name}: {self.message[:20]}..."


class Image(models.Model):
    image_file = models.ImageField(upload_to='images/')  # Store image in the 'images/' directory within media folder
    status_message = models.ForeignKey(StatusMessage, on_delete=models.CASCADE)  # ForeignKey relationship to StatusMessage
    timestamp = models.DateTimeField(default=timezone.now)  # When the image was uploaded

    def __str__(self):
        # String representation for the admin and other use cases
        return f"Image for StatusMessage ID: {self.status_message.id} - Uploaded on {self.timestamp}"
