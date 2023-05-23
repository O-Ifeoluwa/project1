from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    '''profile class'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics')

    def __str__(self):
        '''dunder'''
        return f'{self.user.username} Profile'