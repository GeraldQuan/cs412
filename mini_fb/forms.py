from django import forms
from .models import Profile, StatusMessage

class CreateStatusMessageForm(forms.ModelForm):
    class Meta:
        model = StatusMessage
        fields = ['message']  # The field to be filled out

class CreateProfileForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    city = forms.CharField(label="City", required=True)
    email = forms.EmailField(label="Email", required=True)
    profile_image_url = forms.URLField(label="Profile Image URL", required=True)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'city', 'email', 'profile_image_url']

# New form to update profiles (excluding first and last name)
class UpdateProfileForm(forms.ModelForm):
    city = forms.CharField(label="City", required=True)
    email = forms.EmailField(label="Email", required=True)
    profile_image_url = forms.URLField(label="Profile Image URL", required=True)

    class Meta:
        model = Profile
        fields = ['city', 'email', 'profile_image_url']  # Excluding first_name and last_name

