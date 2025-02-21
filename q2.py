# Question 2: Do Django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production-ready, we just need to understand your logic.
# Yes, by default, Django signals run in the same thread as the caller. This means that the signal handlers are executed in the same thread that sends the signal.

#Code Snippet:

import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import MyModel

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print(f"Signal handler thread: {threading.current_thread().name}")

# In your Django shell or view, save an instance of MyModel
print(f"Main thread: {threading.current_thread().name}")
instance = MyModel.objects.create(field1='value1')

# Explanation:
# When we run this code, we will see that the thread name printed in the signal handler is the same as the main thread name, indicating that they run in the same thread.