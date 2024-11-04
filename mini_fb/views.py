from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse, reverse_lazy
from django.views import View
from django.shortcuts import get_object_or_404, redirect
from .models import Profile, StatusMessage, Image
from .forms import CreateProfileForm, CreateStatusMessageForm, UpdateProfileForm

# View for creating a new status message with file uploads
class CreateStatusMessageView(LoginRequiredMixin, CreateView):
    model = StatusMessage
    form_class = CreateStatusMessageForm
    template_name = 'mini_fb/create_status_form.html'

    def get_object(self):
        return self.request.user.profile

    def form_valid(self, form):
        profile = self.get_object()
        form.instance.profile = profile

        # Save the status message first
        sm = form.save()

        # Handle file uploads
        files = self.request.FILES.getlist('files')
        for file in files:
            image = Image(image_file=file, status_message=sm)
            image.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('show_profile')


# View for updating an existing status message
class UpdateStatusMessageView(LoginRequiredMixin, UpdateView):
    model = StatusMessage
    form_class = CreateStatusMessageForm
    template_name = 'mini_fb/update_status_form.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.profile.user != self.request.user:
            raise HttpResponseForbidden("You are not allowed to edit this status message.")
        return obj

    def get_success_url(self):
        return reverse('show_profile')


# View for deleting an existing status message
class DeleteStatusMessageView(LoginRequiredMixin, DeleteView):
    model = StatusMessage
    template_name = 'mini_fb/delete_status_form.html'
    context_object_name = 'status_message'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.profile.user != self.request.user:
            raise HttpResponseForbidden("You are not allowed to delete this status message.")
        return obj

    def get_success_url(self):
        return reverse_lazy('show_profile')


# View for updating an existing profile
class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'mini_fb/update_profile_form.html'

    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)

    def get_success_url(self):
        return reverse('show_profile')


# View for creating a new profile with User registration
class CreateProfileView(CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'

    def get_context_data(self, **kwargs):
        # Get context and add UserCreationForm to it
        context = super().get_context_data(**kwargs)
        context['user_form'] = UserCreationForm()
        return context

    def form_valid(self, form):
        # Reconstruct UserCreationForm with POST data
        user_form = UserCreationForm(self.request.POST)
        
        if user_form.is_valid():
            # Save User form and get User instance
            user = user_form.save()
            form.instance.user = user  # Attach User to Profile
            
            # Log the user in after registration
            login(self.request, user)
            
            # Continue saving the Profile form
            return super().form_valid(form)
        else:
            # If User form is invalid, render form with errors
            return self.form_invalid(form)
    
    def get_success_url(self):
        return reverse('show_profile')


# View for showing a profile page
class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'mini_fb/show_profile.html'
    context_object_name = 'profile'


# View for showing all profiles
class ShowAllProfilesView(ListView):
    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles'


# View for adding a friend relationship
class CreateFriendView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        profile = request.user.profile
        other_profile = get_object_or_404(Profile, pk=self.kwargs['other_pk'])
        profile.add_friend(other_profile)
        return redirect('show_profile')


# View for displaying friend suggestions
class ShowFriendSuggestionsView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'mini_fb/friend_suggestions.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        context['suggested_friends'] = profile.get_friend_suggestions()
        return context


# View for displaying the news feed
class ShowNewsFeedView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'mini_fb/news_feed.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        context['news_feed'] = profile.get_news_feed()
        return context


# About and Contact views
class AboutView(TemplateView):
    template_name = 'mini_fb/about.html'


class ContactView(TemplateView):
    template_name = 'mini_fb/contact.html'
