from django.conf import settings
from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=256)
    image = models.TextField()
    subtitle = models.CharField(max_length=256)   
    pubDate = models.CharField(max_length=256)
    userRating = models.FloatField()


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    rank = models.FloatField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_reviews")



class Genre(models.Model):
    name = models.CharField(max_length=256)