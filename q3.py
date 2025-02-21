# Question 3: By default do Django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production-ready, we just need to understand your logic.
# Yes, by default, Django signals run in the same database transaction as the caller. This means that if the signal is sent within a transaction, the signal handlers are executed within that transaction.

# Code Snippet:

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import MyModel

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print(f"Inside transaction: {transaction.get_connection().in_atomic_block}")

# In your Django shell or view, save an instance of MyModel within a transaction
with transaction.atomic():
    instance = MyModel.objects.create(field1='value1')
    print(f"Inside transaction: {transaction.get_connection().in_atomic_block}")

# Explanation:
# When we run this code, we will see that both prints inside and outside the signal handler indicate that they are within a transaction (in_atomic_block is True), showing that the signal handler runs in the same transaction.