# built-in/default model creation class
from django.db import models

# built-in/default USER model object
from django.contrib.auth.models import User

# django utility for register post time
from django.utils import timezone

# reverse != redirect
# redirect function redirects to a specific route
# reverse only returns the route/url as a string
from django.urls import reverse

class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # if the user is deleted, his/her posts will be deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # DJANGO MANDATORY METHOD
    # create method to redirect to a particular url
    def get_absolute_url(self):
        # RETURN THE URL FOR THE VIEW (+ POST object primary key) TO HANDLE THE REDIRECTION
        return reverse('post-detail', kwargs={'pk': self.pk})
