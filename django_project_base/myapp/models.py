from django.db import models
import threading
import time
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class TestModel(models.Model):
    value = models.IntegerField(default=0)

@receiver(post_save, sender=TestModel)
def signal_handler(sender, instance, **kwargs):
    print(f"[Signal] Thread ID: {threading.get_ident()}")
    start = time.time()
    # Simulate CPU-bound task to show blocking behavior
    result = sum(i*i for i in range(10**6))
    end = time.time()
    print(f"[Signal] Computation done in {end - start:.2f}s, result={result}")

# Create your models here.
