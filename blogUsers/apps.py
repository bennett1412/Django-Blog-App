from django.apps import AppConfig


class BlogusersConfig(AppConfig):
    name = 'blogUsers'

    def ready(self):
        import blogUsers.signals