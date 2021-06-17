from django.db.models.signals import pre_save, post_save
from .models import Order, Stock

def validate_order(sender, instance, **kwargs):

    if instance.quantity < instance.stock_item.quantity:
        # order can be fulfilled
        # quit items from stock
        q_ordered = instance.quantity
        q_stock = instance.stock_item.quantity
        stock = Stock.objects.filter(id=instance.stock_item.id).first()
        stock.quantity = q_stock - q_ordered
        stock.save() 
    else:
        print('No Stock!')


def notify_user(sender, instance, **kwargs):
   print('Email sent to consumer')


pre_save.connect(validate_order, sender=Order)
post_save.connect(notify_user, sender=Order)