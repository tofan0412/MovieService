from rest_framework import serializers
from .models import Movie, Review


class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'rank', 'liked_users')

# class RateSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Movie
#         fields = ('userRating')
        