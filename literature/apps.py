from django.apps import AppConfig


class LiteratureConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'literature'
    
    def ready(self):
        import literature.signals
