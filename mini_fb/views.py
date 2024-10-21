from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Profile, StatusMessage, Image
from .forms import CreateProfileForm, CreateStatusMessageForm, UpdateProfileForm

# View for creating a new status message with file uploads
class CreateStatusMessageView(CreateView):
    model = StatusMessage
    form_class = CreateStatusMessageForm
    template_name = 'mini_fb/create_status_form.html'

    # Provide the profile to the form via context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(pk=self.kwargs['pk'])  # Get the profile using pk
        return context

    # Attach the status message to the profile and handle image uploads
    def form_valid(self, form):
        profile = Profile.objects.get(pk=self.kwargs['pk'])  # Get the profile to attach the status message
        form.instance.profile = profile  # Attach the profile to the status message

        # Save the status message first
        sm = form.save()

        # Handle file uploads
        files = self.request.FILES.getlist('files')  # Get list of uploaded files
        for file in files:
            image = Image(image_file=file, status_message=sm)  # Create Image object for each file
            image.save()  # Save image to the database
        
        return super().form_valid(form)

    # After submission, redirect to the profile page
    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.kwargs['pk']})


# View for updating an existing status message
class UpdateStatusMessageView(UpdateView):
    model = StatusMessage
    form_class = CreateStatusMessageForm
    template_name = 'mini_fb/update_status_form.html'

    def get_success_url(self):
        # Redirect back to the profile page after updating
        return reverse('show_profile', kwargs={'pk': self.object.profile.pk})


# View for deleting an existing status message
class DeleteStatusMessageView(DeleteView):
    model = StatusMessage
    template_name = 'mini_fb/delete_status_form.html'
    context_object_name = 'status_message'

    def get_success_url(self):
        # Redirect to the profile page after deletion
        return reverse_lazy('show_profile', kwargs={'pk': self.object.profile.pk})


# View for updating an existing profile
class UpdateProfileView(UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'mini_fb/update_profile_form.html'

    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.object.pk})


# View for creating a new profile
class CreateProfileView(CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'

    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.object.pk})


# View for showing a profile page
class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'mini_fb/show_profile.html'  # Pointing to the template for profile display
    context_object_name = 'profile'  # The context name in the template


# View for showing all profiles
class ShowAllProfilesView(ListView):
    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        # Auto-create profiles for testing purposes if none exist
        if Profile.objects.count() == 0:
            Profile.objects.create(
                first_name="Lionel", last_name="Messi", city="Rosario",
                profile_image_url="https://upload.wikimedia.org/wikipedia/commons/b/b4/Lionel-Messi-Argentina-2022-FIFA-World-Cup_%28cropped%29.jpg"
            )
            Profile.objects.create(
                first_name="LeBron", last_name="James", city="Akron",
                profile_image_url="https://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/1966.png"
            )
        return Profile.objects.all()

