# Django Signals - Database Transaction Behavior

## Question 3: By default, do Django signals run in the same database transaction as the caller?

### Answer:
Yes, by default, **Django signals run in the same database transaction as the caller**. This means if the main transaction is rolled back (e.g., due to an error), any database changes made inside the signal handler are also rolled back. Signal handlers do **not run in isolation** unless you explicitly make them do so.

---

## Proof with Code Snippet:

We prove this by:
- Creating two models: `MainModel` and `LogModel`
- Inside a signal, we create a `LogModel` entry after saving a `MainModel` instance
- We then **force a transaction rollback** using `transaction.atomic()` and raise an exception
- Finally, we check if the `LogModel` entry still exists (it shouldn't if the signal was part of the transaction)

---

### models.py
```python
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
