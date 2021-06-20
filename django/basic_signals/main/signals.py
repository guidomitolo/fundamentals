# any signal
from django.core.signals import request_finished

# signal = request, receives from any sender
def my_callback(sender, **kwargs):
    print("Signals activated! Request finished!")

# Signal.connect(receiver, sender=None, weak=True, dispatch_uid=None)
request_finished.connect(my_callback)