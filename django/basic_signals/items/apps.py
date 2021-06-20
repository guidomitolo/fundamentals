from django.apps import AppConfig


class ItemsConfig(AppConfig):
    name = 'items'

    # https://docs.djangoproject.com/en/3.2/ref/applications/#django.apps.AppConfig.ready
    def ready(self):
        import items.signals