from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import MovieSerializer, ReviewSerializer
from .models import Movie, Review
import requests


@api_view(['GET'])  #일단 GET방식 테스트
def index(request):
    movies = Movie.objects.all()
    serializers = MovieSerializer(movies, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializers = MovieSerializer(movie)
    return Response(serializers.data)


@api_view(['GET'])
def review_list(request, movie_pk):
    reviews = Review.objects.filter(movie_id=movie_pk)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


def trailer(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    input = movie.subtitle + 'trailer'
    url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'key': 'AIzaSyC4uHRgq7maECpf4WEkbDjKwhRc6G7Xlk8',
        'part': 'snippet',
        'type': 'video',
        'maxResults': '1',        
        'q': input
    }
    response = requests.get(url, params)
    response_dic = response.json() # Json response이므로 딕셔너리 타입으로 변환
    data = {
        'YoutubeItem': response_dic['items']
    }
    return JsonResponse(data) #response를 커스터마이징 후에 전달하고 싶어서 사용


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication]) 
@permission_classes([IsAuthenticated]) 
def review_list_create(request, movie_pk):
    movie = get_object_or_404(Movie, id=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie=movie)
        return Response(serializer.data)


@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication]) 
@permission_classes([IsAuthenticated]) 
def review_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    review.delete()
    return Response({'id': review_pk})


@api_view(['PUT'])
@authentication_classes([JSONWebTokenAuthentication]) 
@permission_classes([IsAuthenticated]) 
def review_update(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    # review.delete()
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, review=review)
        return Response(serializer.data)


@authentication_classes([JSONWebTokenAuthentication]) 
@permission_classes([IsAuthenticated]) 
def like(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    if movie.like_users.filter(pk=user.pk).exists(): #이미 좋아요했으면 취소
        movie.like_users.remove(user)
        liked = False  
    else:
        movie.like_users.add(user)
        liked = True
        
    count = movie.like_users.count()
    data = {
        'liked': liked,
        'count': count,
    }
    return JsonResponse(data)
