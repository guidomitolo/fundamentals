from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'

    # https://docs.djangoproject.com/en/3.2/ref/applications/#django.apps.AppConfig.ready
    def ready(self):
        import main.signals
