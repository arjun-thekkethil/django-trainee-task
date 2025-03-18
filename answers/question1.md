# Django Signals - Execution Behavior

## Question 1: Are Django signals executed synchronously or asynchronously?

### Answer:
In Django, signals are **executed synchronously by default**. This means as soon as a signal is triggered, its connected handler runs **immediately**, and your code will **wait for it to finish** before continuing. The handler and the sender run in the **same execution flow**, so if the signal takes time, it directly affects the performance of the code that sent it.

---

## Proof with Code Snippet:

We verify this by:
- Printing the **Thread ID** of the main code and signal handler
- Running a **CPU-bound task** inside the signal to simulate real work
- Measuring total execution time to show blocking behavior

---

### models.py
```python
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
    result = sum(i*i for i in range(10**6))  # Simulate work
    end = time.time()
    print(f"[Signal] Computation done in {end - start:.2f}s, result={result}")
