from django.conf import settings
from django.core import paginator
from django.core.paginator import Paginator
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import MovieSerializer, ReviewSerializer
from .models import Genre, Movie, Review
import requests


@api_view(['GET'])
def index(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 10)
    print(paginator)
    page_number = request.GET.get('page')
    
    movies = paginator.get_page(page_number)
    if movies.has_next:
        pass
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
    # return HttpResponse(status=status.)


@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication]) 
@permission_classes([IsAuthenticated]) 
def review_delete(request, review_pk):
    user = request.user
    # 본인이 아닌 사용자가 삭제하려고 하는 경우, 반환한다.
    review = get_object_or_404(Review, pk=review_pk)
    if not (user.username == review.user_id):
        return HttpResponse(status=status.status.HTTP_401_UNAUTHORIZED)
    
    if user != review.user_id:
        return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)

    review.delete()
    return Response({'id': review_pk})


@api_view(['PUT'])
@authentication_classes([JSONWebTokenAuthentication]) 
@permission_classes([IsAuthenticated]) 
def review_update(request, review_pk):
    user = request.user
    review = get_object_or_404(Review, pk=review_pk)
    
    # 본인이 아니라면 수정할 수 없다.
    if not (user.username == review.user_id):
        return HttpResponse(status=status.status.HTTP_401_UNAUTHORIZED)

    serializer = ReviewSerializer(review, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
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


@api_view(['POST'])
def recommend(request):
    genres = Genre.objects.all()
    
    test = Movie.objects.all()
    q1 = Movie.objects.none()
    # genre 별로 영화를 가져온다. 
    for genre in genres:
        genreObj = get_object_or_404(Genre, pk=genre.id)
        q2 = genreObj.movies.order_by('?')[:5]
        q1 = q1 | q2

    serializer = MovieSerializer(q1, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication]) 
@permission_classes([IsAuthenticated]) 
def favorite_create(request):
    # 각 영화에 대해 genre를 불러온다..
    genres = []
    for movie_id in request.data: 
        movie = get_object_or_404(Movie, pk=movie_id)
        for genre in movie.genres.all():
            # 장르가 중복되어선 안된다.
            if genre not in genres:
                genres.append(genre)
    
    user = request.user
    for genre in genres:
        # 이미 있으면 넣으면 안된다.
        if user.like_genres.filter(pk=genre.id).exists():
            pass
        else:
            user.like_genres.add(genre)

    return HttpResponse(status=status.HTTP_201_CREATED)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication]) 
@permission_classes([IsAuthenticated]) 
def favorite_list_user(request):
    # 사용자가 선택한 genre 기반으로 영화 데이터를 추출한다.
    user = request.user
    genres = user.like_genres.order_by('?')[:1] # 사용자가 선택한 장르 중에서 임의로 하나 불러오기.
    
    # 만약 사용자가 추천 영화를 선택하지 않았다면? 평점 기반으로 영화를 추천한다.
    if len(genres) == 0:
        movies = Movie.objects.filter(userRating__gte=8.0).order_by('?')[:5]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    # 사용자가 장르를 선택한 경우에는, 장르 기반으로 영화를 추천한다.
    else:
        genre_dict = genres.values()
        genre_id = genre_dict[0]['id']
        
        genre = get_object_or_404(Genre, pk=genre_id)
        movies = genre.movies.order_by('?')[:5]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    

@api_view(['POST'])
def favorite_list_anonymousUser(request):
    # 평점 8.5 이상인 영화를 기반으로 영화 데이터를 추출한다.
    movies = Movie.objects.filter(userRating__gte=8.0).order_by('?')[:5]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication]) 
@permission_classes([IsAuthenticated])
def like(request): 
    user = request.user
    movie = get_object_or_404(Movie, pk=request.data['id'])
    
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        return JsonResponse({'status': status.HTTP_204_NO_CONTENT})
    else:
        movie.like_users.add(user)
        return JsonResponse({'status': status.HTTP_202_ACCEPTED})
    

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication]) 
@permission_classes([IsAuthenticated])
def check_like(request):
    user = request.user
    movie = get_object_or_404(Movie, pk=request.data['id'])
    
    if movie.like_users.filter(pk=user.pk).exists():
        return JsonResponse({'status': status.HTTP_202_ACCEPTED})
    else:
        return JsonResponse({'status': status.HTTP_204_NO_CONTENT})
