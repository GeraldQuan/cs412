from django import forms
from .models import Profile
from .models import StatusMessage

class CreateStatusMessageForm(forms.ModelForm):
    class Meta:
        model = StatusMessage
        fields = ['message']  # The field to be filled out

class CreateProfileForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    bio = forms.CharField(label="Bio", widget=forms.Textarea, required=True)
    dob = forms.DateField(widget=forms.SelectDateWidget(years=range(2024, 1920, -1)))
    profile_image_url = forms.URLField(label="Profile Image URL", required=True)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'bio', 'dob', 'profile_image_url'] 

