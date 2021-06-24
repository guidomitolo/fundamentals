from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Books(models.Model):

    GENRE = (
        ('Non Fiction', 'Non Fiction'),
        ('Fantasy', 'Fantasy'),
        ('Science Fiction', 'Science Fiction'),
        ('History', 'History')
    )

    # related_name -> name to the reverse relationship from Users
    # ¿Which books did the librarian loaded?
    librarian = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books")

    author = models.CharField('Author', max_length=128, null=True, blank=True)
    title = models.CharField('Title', max_length=128, null=True, blank=True)
    genre = models.CharField('Genre', max_length=64, choices=GENRE, null=True, blank=True)
    price = models.PositiveIntegerField('Price', null=True, blank=True)
