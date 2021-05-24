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
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializers = MovieSerializer(movie)
    return Response(serializers.data)


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def rank_list_create(request, movie_pk):
    movie = get_object_or_404(Review, id=movie_pk)
    if request.method=='GET':
        reviews = movie.objects.all()
        serializer= ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    else:
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data)


@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def rank_delete(request, movie_pk):
    review = get_object_or_404(Review, pk=movie_pk)
    review.delete()
    return Response({'id': movie_pk})


@api_view(['PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def rank_update(request, movie_pk):
    review = get_object_or_404(Review, id=movie_pk)  
    rank = get_object_or_404(Review, user=request.user)
    rank.delete()
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, review=review)
        return Response(serializer.data)


# 좋아요 추가 예정

    