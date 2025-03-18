import threading
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class TestModel(models.Model):
    value = models.IntegerField(default=0)

@receiver(post_save, sender=TestModel)
def signal_handler(sender, instance, **kwargs):
    print(f"[Signal] Running in Thread ID: {threading.get_ident()}")
