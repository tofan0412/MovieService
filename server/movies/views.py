from django.http.response import JsonResponse
# from server.community import serializers
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import MovieSerializer, ReviewSerializer
from .models import Movie, Review


@api_view(['GET'])  #일단 GET방식 테스트
def index(request):
    movies = Movie.objects.all()
    serializers = MovieSerializer(movies, many=True)
    return Response(serializers.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication]) # 로그인 했는가? (인증했는가?)
@permission_classes([IsAuthenticated]) # 인증이 된 상태에서만 권한이 부여된다.
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializers = MovieSerializer(movie)
    return Response(serializers.data)


@api_view(['GET'])
def review_list(request, movie_pk):
    reviews = Review.objects.filter(movie_id=movie_pk)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


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
def like(request, review_pk):
    user = request.user
    review = get_object_or_404(Review, pk=review_pk)
    
    if review.liked_users.filter(pk=user.pk).exists(): #이미 좋아요했으면 취소
        review.liked_users.remove(user)
        liked = False  
    else:
        review.liked_users.add(user)
        liked = True
        
    count = review.liked_users.count()
    data = {
        'liked': liked,
        'count': count,
    }
    return JsonResponse(data)
