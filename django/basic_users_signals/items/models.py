from django.db import models

# Create your models here.
class Stock(models.Model):
    product = models.CharField('Product', max_length=20, unique=True)
    price =  models.FloatField('Price')
    quantity = models.IntegerField('Amount')

    def __str__(self):
        return f"Stock: {self.product} ({self.quantity} items)"


class Order(models.Model):
    stock_item = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField('Amount')

    def __str__(self):
        return f"Order: {self.stock_item.product} ({self.quantity} items)"