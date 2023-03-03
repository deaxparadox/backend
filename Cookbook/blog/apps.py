from django.apps import AppConfig
from django.core.signals import setting_changed

import rich 
from rich.panel import Panel 

def my_callback(sender, **kwargs):
    # print("Setting changed!")
    rich.print(
        Panel.fit("Setting changed!!!", style='red')
    )

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        setting_changed.connect(my_callback)