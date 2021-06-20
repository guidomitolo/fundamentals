from django.db import models

# Create your models here.
class Stock(models.Model):
    product = models.CharField('Product', max_length=20, unique=True)
    unit_price =  models.FloatField('Price')
    quantity = models.IntegerField('Amount')

    def __str__(self):
        return f"Stock: {self.product} ({self.quantity} items)"


class Order(models.Model):
    stock_item = models.ForeignKey(Stock, on_delete=models.CASCADE, verbose_name='Product')
    quantity = models.IntegerField('Amount', null=True)
    total_price = models.FloatField('Total price', null=True)
    trans_id = models.CharField('Transaction Id', max_length=10, blank=True)

    # override save method to check stock
    def save(self, *args, **kwards):
        if self.quantity > self.stock_item.quantity:
            return False
        return super().save(*args, **kwards)

    def __str__(self):
        return f"Order: {self.stock_item.product} ({self.quantity} items)"