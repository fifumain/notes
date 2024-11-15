from django.apps import AppConfig


class NotesAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.notes_app"

    def ready(self):
        import core_apps.notes_app.signals
