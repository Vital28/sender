from django.apps import AppConfig


class SendingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sending"

    def ready(self):
        from sending import signals
