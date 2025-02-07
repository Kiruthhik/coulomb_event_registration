from django.apps import AppConfig


class EventRegistrationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'event_registration'

    def ready(self):
        import event_registration.signals  # Import signals when the app is ready