from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.db.models import Q

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
 # Allow null initially for migration
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    profile_image_url = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_status_messages(self):
        return self.statusmessage_set.all().order_by('-timestamp')

    def get_absolute_url(self):
        return reverse('show_profile', kwargs={'pk': self.pk})

    def get_friends(self):
        friends = Friend.objects.filter(Q(profile1=self) | Q(profile2=self))
        friend_profiles = [
            friend.profile2 if friend.profile1 == self else friend.profile1
            for friend in friends
        ]
        return friend_profiles

    def add_friend(self, other):
        if self == other:
            return
        if not Friend.objects.filter(
            (Q(profile1=self) & Q(profile2=other)) | (Q(profile1=other) & Q(profile2=self))
        ).exists():
            Friend.objects.create(profile1=self, profile2=other)

    def get_friend_suggestions(self):
        all_profiles = Profile.objects.exclude(id=self.id)
        current_friends = self.get_friends()
        suggested_friends = all_profiles.exclude(id__in=[friend.id for friend in current_friends])
        return suggested_friends

    def get_news_feed(self):
        friends = self.get_friends()
        profiles = [self] + friends
        news_feed = StatusMessage.objects.filter(profile__in=profiles).order_by('-timestamp')
        return news_feed


class StatusMessage(models.Model):
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def get_images(self):
        return self.image_set.all()

    def __str__(self):
        return f"{self.profile.first_name} {self.profile.last_name}: {self.message[:20]}..."


class Image(models.Model):
    image_file = models.ImageField(upload_to='images/')
    status_message = models.ForeignKey(StatusMessage, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Image for StatusMessage ID: {self.status_message.id} - Uploaded on {self.timestamp}"


class Friend(models.Model):
    profile1 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile1')
    profile2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile2')
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.profile1.first_name} {self.profile1.last_name} & {self.profile2.first_name} {self.profile2.last_name}"