
from django.views.generic import ListView
from .models import Profile

class ShowAllProfilesView(ListView):
    model = Profile
    template_name = 'show_all_profiles.html'
    context_object_name = 'profiles'


    def get_queryset(self):
        print("Creating profiles if none exist...")  
        if Profile.objects.count() == 0:
            Profile.objects.create(
                first_name="Lionel", last_name="Messi", city="Rosario",
                profile_image_url="https://www.google.com/url?sa=i&url=https%3A%2F%2Fplayers.fcbarcelona.com%2Fen%2Fplayer%2F548-messi-lionel-andres-messi-cuccitini&psig=AOvVaw00HlIjQPSty9ZShebJSciJ&ust=1728430809849000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCKi7zNW4_YgDFQAAAAAdAAAAABAE"
            )
            Profile.objects.create(
                first_name="LeBron", last_name="James", city="Akron",
                profile_image_url="https://www.google.com/url?sa=i&url=https%3A%2F%2Fhoopshype.com%2F2024%2F01%2F25%2Flebron-james-becomes-first-player-ever-with-20-nba-all-star-game-selections%2F&psig=AOvVaw2MXDTogp-DCWHEc_UYzqtK&ust=1728430836924000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCMD-jOK4_YgDFQAAAAAdAAAAABAE"
            )
            Profile.objects.create(
                first_name="Michael", last_name="Jordan", city="Brooklyn",
                profile_image_url="https://upload.wikimedia.org/wikipedia/commons/a/ae/Michael_Jordan_in_2014.jpg"
            )
            Profile.objects.create(
                first_name="Kobe", last_name="Bryant", city="Philadelphia",
                profile_image_url="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.biography.com%2Fathletes%2Fkobe-bryant&psig=AOvVaw2k5UEIiLvD1abi5wVHYz95&ust=1728430870155000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCND6ofK4_YgDFQAAAAAdAAAAABAE"
            )
            Profile.objects.create(
                first_name="Jinping", last_name="Xi", city="Beijing",
                profile_image_url="https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FXi_Jinping&psig=AOvVaw3xWSEao-h0l4M-QJRw3W0z&ust=1728430888091000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOCvvPq4_YgDFQAAAAAdAAAAABAE"
            )
        
        
        return Profile.objects.all()
