# any signal
from django.core.signals import request_finished
# model signals
from django.db.models.signals import post_save

from django.contrib.auth.models import User


# signal = request, receives from any sender
def my_callback(sender, **kwargs):
    print("Signals activated! Request finished!")

# Signal.connect(receiver, sender=None, weak=True, dispatch_uid=None)
request_finished.connect(my_callback)

######

# signal = save method, receives from User model
def register_signal(sender, **kwargs):
    print("Signals activated! A new user is registered!")

# Signal.connect(receiver, sender=None, weak=True, dispatch_uid=None)
post_save.connect(register_signal, sender=User)