from django.conf import settings
from django.db import models

# Create your models here.
class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)


class Movie(models.Model):
    title = models.CharField(max_length=256)
    image = models.TextField()
    subtitle = models.CharField(max_length=256)   
    overview = models.TextField()
    pubDate = models.CharField(max_length=256)
    userRating = models.FloatField()
    genres = models.ManyToManyField(Genre, related_name="movies")
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    rank = models.FloatField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)