# ?Question 1: By default are Django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production-ready, we just need to understand your logic.
# Answer: By default, Django signals executed synchronously. This means that when a signal is sent, the connected receivers i.e. signal handlers are executed immediately in the same process.
# Code Snippet:

import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import MyModel

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print("Signal received. Starting processing...")
    time.sleep(5)  # Simulate a long-running task
    print("Processing complete.")

# In your Django shell or view, save an instance of MyModel
instance = MyModel.objects.create(field1='value1')

print("Instance saved.")

# Explanation:
# When we run this code, we will see "Signal received. Starting processing..." printed immediately after "Instance saved." This indicates that the signal handler is executed synchronously, as the main thread waits for the handler to complete before proceeding.