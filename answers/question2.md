# Django Signals - Thread Execution Behavior

## Question 2: Do Django signals run in the same thread as the caller?

### Answer:
Yes, by default, **Django signals run in the same thread as the caller**. This means when a signal is triggered, its handler function **executes immediately in the same thread** — there is no thread switching or asynchronous behavior unless explicitly introduced.

---

## Proof with Code Snippet:

To confirm this, we print the **Thread ID** of the caller and the signal handler. If both IDs match, it proves they run in the **same thread**.

---

### models.py
```python
import threading
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class TestModel(models.Model):
    value = models.IntegerField(default=0)

@receiver(post_save, sender=TestModel)
def signal_handler(sender, instance, **kwargs):
    print(f"[Signal] Running in Thread ID: {threading.get_ident()}")
