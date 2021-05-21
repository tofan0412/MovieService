from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieSerializer
from .models import Movie
# import requests

@api_view(['GET'])  #일단 GET방식 테스트
def index(request):
    # client_id = "cTouCjNxX9puRsipWcFz"
    # client_secert = "vSOn9KESoJ"
    # URL = 'https://openapi.naver.com/v1/search/movie.json?display=100&query=어밴저스&start=1&pubDate="2021"' 
    # request = urllib.request.Request(URL) 
    # request.add_header("X-Naver-Client-Id", client_id)
    # request.add_header("X-Naver-Client-Secret", client_secert)

    movies = Movie.objects.all()
    serializers = MovieSerializer(movies, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializers = MovieSerializer(movie)
    return Response(serializers.data)