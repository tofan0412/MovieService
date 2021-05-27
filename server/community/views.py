from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer
from django.http.response import HttpResponse
from rest_framework import status


@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer= ArticleSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication]) # 토큰 유효한지 확인
@permission_classes([IsAuthenticated]) 
def articlelist_create(request): 
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def article_update_delete(request, article_pk): 
    user = request.user
    article = get_object_or_404(Article, pk=article_pk)    

    if not (user.username == article.user_id):
        return HttpResponse(status=status.status.HTTP_401_UNAUTHORIZED)

    if request.method=='PUT' : 
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True): 
            serializer.save()
            return Response(serializer.data)
    else:
        if user != article.user_id:
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)

        article.delete()
        return Response({'id':article_pk})
        

@api_view(['GET'])
def comment_list(request, article_pk):
    comments = Comment.objects.filter(article_id=article_pk)
    serializer= CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_list_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article=article) #article의 내용을 바꿔줘야하므로 article = article
        return Response(serializer.data)


@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_delete(request, comment_pk):
    user = request.user
    comment = get_object_or_404(Comment, pk=comment_pk)    

    if not (user.username == comment.user_id):
        return HttpResponse(status=status.status.HTTP_401_UNAUTHORIZED)

    if user != comment.user_id:
        return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)

    comment.delete()
    return Response({'id': comment_pk})

