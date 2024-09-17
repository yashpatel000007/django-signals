# myapp/models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading
import time
from django.db import transaction

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    # For Question 1 and 2
    print(f"Signal handler is running in thread: {threading.current_thread().name}")
    print("Signal handler started")
    time.sleep(5)  # Simulate a delay
    print("Signal handler finished")

    # For Question 3
    with transaction.atomic():
        print(f"Transaction status: {transaction.get_connection().in_atomic_block}")
