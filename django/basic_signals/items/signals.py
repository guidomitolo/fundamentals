from django.db.models.signals import pre_save, post_save
from .models import Order, Stock
import copy
import random

# sender = object
# instance = the object/sender instantiated

# pre save example
def add_id_price(sender, instance, **kwargs):
    instance.total_price = instance.stock_item.unit_price * instance.quantity
    instance.trans_id = str(random.randrange(0, 9999999999))

# post save example
def update_stock(sender, instance, **kwargs):
    # update items from stock
    stock = Stock.objects.filter(id=instance.stock_item.id).first()
    stock.quantity = stock.quantity - instance.quantity
    stock.save()

# post save example
def notify_user(sender, instance, **kwargs):
   print('Email sent to client!')


pre_save.connect(add_id_price, sender=Order)
post_save.connect(update_stock, sender=Order)
post_save.connect(notify_user, sender=Order)
