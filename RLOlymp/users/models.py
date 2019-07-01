from django.db import models
from django.contrib.auth.models import User
from django.core.cache import cache 
from RLOlymp import settings
from django.urls import reverse

import datetime

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default='media/default.png', upload_to='media/user_images')
    solved_problems = models.IntegerField(default=0)
    shipments = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username}'
