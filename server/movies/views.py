from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieSerializer, RateSerializer
from .models import Movie


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


## rating 관련 로직

# @api_view(['GET', 'POST'])
# def rate_list_create(request, movie_id):
#     movie = get_object_or_404(Movie, id=movie_id)
#     if request.method=='GET':
#         ratings = movie.userRating.all()
#         serializer= RateSerializer(ratings, many=True)
#         return Response(serializer.data)
#     else:
#         serializer = RateSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(user=request.user, movie=movie)
#             return Response(serializer.data)


# @api_view(['DELETE'])
# def rate_delete(request, rate_pk):
#     rating = get_object_or_404(Movie.userRating, pk=rate_pk)
#     rating.delete()
#     return Response({'id': rate_pk})


# @api_view(['PUT'])
# def rate_update(request, movie_pk):
#     movie = get_object_or_404(Movie, id=movie_pk)
#     rating = get_object_or_404(movie.userRating, user=request.user)
#     rating.delete()
#     serializer = RateSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(user=request.user, movie=movie)
#         return Response(serializer.data)




# 좋아요 추가 예정

    