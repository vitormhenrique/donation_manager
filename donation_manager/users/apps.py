from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "donation_manager.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import donation_manager.users.signals  # noqa F401
        except ImportError:
            pass
