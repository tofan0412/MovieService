from server import movies
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=10, primary_key=True)
    password = models.CharField(max_length=256)
    like_genres = models.ManyToManyField(settings.GENRE_MODEL, related_name='like_users')