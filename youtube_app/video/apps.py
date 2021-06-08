from django.apps import AppConfig
from . import scheduler_data_fetch

class VideoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'video'
    # def ready(self):
    #     print("1")
    #     scheduler_data_fetch.begin()
