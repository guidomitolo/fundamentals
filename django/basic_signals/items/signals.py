from django.db.models.signals import pre_save, post_save
from .models import Order, Stock
import copy
import random

# sender = object
# instance = the object/sender instanciated

# pre save example
def add_transcation_id(sender, instance, **kwargs):
    if instance.trans_id == '':
        instance.trans_id = str(random.randrange(0, 9999999999))

# post save example
def update_stock(sender, instance, **kwargs):
    # update items from stock
    stock = Stock.objects.filter(id=instance.stock_item.id).first()
    stock.quantity = stock.quantity - instance.quantity
    # contrary to pre_save it is mandatory to evoke .save method in post_save
    stock.save()

# post save example
def notify_user(sender, instance, **kwargs):
   print('Email sent to client!')


pre_save.connect(add_transcation_id, sender=Order)
post_save.connect(update_stock, sender=Order)
post_save.connect(notify_user, sender=Order)
