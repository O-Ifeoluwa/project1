from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Posts(models.Model):
    '''post characteristics'''
    topic = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.topic