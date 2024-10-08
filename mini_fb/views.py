
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
