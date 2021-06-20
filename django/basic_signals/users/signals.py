# model signals
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Client


# signal = object
# instance = the object/sender instanciated
# created = True if sender is being created for the first time
def user_reg_signal(sender, instance, created, **kwargs):
    if created:
        print("Signals activated! A new user is registered!")
        Client.objects.create(user=instance)


# Signal.connect(receiver, sender=None, weak=True, dispatch_uid=None)
post_save.connect(user_reg_signal, sender=User)