from django.db import models

# Create your models here.
class Houses(models.Model):
    published = models.DateTimeField(auto_now_add=True)
    street = models.CharField(max_length=64, null=True, blank=True)
    adress = models.PositiveIntegerField(null=True, blank=True)
    room = models.PositiveIntegerField(null=True, blank=True)
    m2 = models.PositiveIntegerField(null=True, blank=True)
    pool = models.BooleanField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ['published']

    def __str__(self,):
        return f'{self.street} {self.adress}'
 
