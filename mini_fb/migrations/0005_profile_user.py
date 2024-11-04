import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


def assign_users_to_existing_profiles(apps, schema_editor):
    Profile = apps.get_model('mini_fb', 'Profile')
    User = apps.get_model(settings.AUTH_USER_MODEL)

    # Iterate through profiles that lack a user and assign a unique User
    for profile in Profile.objects.filter(user__isnull=True):
        # Either find an unused user or create a new dummy user if needed
        available_user = User.objects.exclude(id__in=Profile.objects.values_list('user', flat=True)).first()
        if not available_user:
            # Create a new dummy user if no unused user is available
            available_user = User.objects.create(username=f"user_for_profile_{profile.id}")
        profile.user = available_user
        profile.save()


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0004_friend'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        # Step 1: Add the user field with null=True to avoid immediate NOT NULL constraint
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        # Step 2: Run a data migration to assign users to all existing profiles
        migrations.RunPython(assign_users_to_existing_profiles),
        # Step 3: Alter the field to make it non-nullable after data migration
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
