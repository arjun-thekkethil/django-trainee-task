from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class MainModel(models.Model):
    name = models.CharField(max_length=100)

class LogModel(models.Model):
    message = models.CharField(max_length=255)

@receiver(post_save, sender=MainModel)
def create_log(sender, instance, **kwargs):
    from django.db import transaction
    LogModel.objects.create(message=f"Created: {instance.name}")
    print("Signal: LogModel entry created")