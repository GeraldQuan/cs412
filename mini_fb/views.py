
from django.views.generic import ListView
from .models import Profile
from django.shortcuts import render
from django.views.generic import DetailView
from .forms import CreateProfileForm
from django.urls import reverse
from django.views.generic import CreateView
from .models import StatusMessage, Profile
from .forms import CreateStatusMessageForm

class CreateStatusMessageView(CreateView):
    model = StatusMessage
    form_class = CreateStatusMessageForm
    template_name = 'mini_fb/create_status_form.html'

    # Provide the profile to the form via context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(pk=self.kwargs['pk'])
        return context

    # Attach the status message to the profile
    def form_valid(self, form):
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        form.instance.profile = profile  # Attach the profile to the status message
        return super().form_valid(form)

    # After submission, redirect to the profile page
    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.kwargs['pk']})


class CreateProfileView(CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'

    def get_success_url(self):
        # Redirect to the newly created profile's page after form submission
        return reverse('show_profile', kwargs={'pk': self.object.pk})


class CreateProfileView(CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'

    def get_success_url(self):
        # Redirect to the newly created profile's page after form submission
        return reverse('show_profile', kwargs={'pk': self.object.pk})

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'show_profile.html'  # Pointing to the template for profile display
    context_object_name = 'profile'  # The context name in the template


class ShowAllProfilesView(ListView):
    model = Profile
    template_name = 'show_all_profiles.html'
    context_object_name = 'profiles'


    def get_queryset(self):
        print("Creating profiles if none exist...")  
        if Profile.objects.count() == 0:
            Profile.objects.create(
                first_name="Lionel", last_name="Messi", city="Rosario",
                profile_image_url="https://upload.wikimedia.org/wikipedia/commons/b/b4/Lionel-Messi-Argentina-2022-FIFA-World-Cup_%28cropped%29.jpg"
            )
            Profile.objects.create(
                first_name="LeBron", last_name="James", city="Akron",
                profile_image_url="https://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/1966.png"
            )
            Profile.objects.create(
                first_name="Michael", last_name="Jordan", city="Brooklyn",
                profile_image_url="https://upload.wikimedia.org/wikipedia/commons/a/ae/Michael_Jordan_in_2014.jpg"
            )
            Profile.objects.create(
                first_name="Kobe", last_name="Bryant", city="Philadelphia",
                profile_image_url="https://cdn.nba.com/headshots/nba/latest/1040x760/977.png"
            )
            Profile.objects.create(
                first_name="Jinping", last_name="Xi", city="Beijing",
                profile_image_url="https://upload.wikimedia.org/wikipedia/commons/0/06/Xi_Jinping_in_July_2024_%28cropped%29.jpg"
            )
        
        
        return Profile.objects.all()
