from django.apps import AppConfig


class ProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project'
    verbose_name = 'Personal Library Management'  # Adds a human-readable name for the app in the admin interface

    def ready(self):
        pass  # Leave this empty if signals are not used
