from django.db import models

# Create your models here.
class Cars(models.Model):

    CONDITION = (
        ('Excelent', 'Excelent'),
        ('Good', 'Good'),
        ('To Repair', 'To Repair'),
    )

    model = models.CharField('Model', max_length=64, null=True, blank=True)
    vendor = models.CharField('Vendor', max_length=64, null=True, blank=True)
    date = models.DateField('Date', null=True, blank=True)
    price = models.FloatField('Price', null=True, blank=True)
    condition = models.CharField(max_length=32, choices=CONDITION, null=True)


    def __str__(self,):
        return f'{self.model}'
