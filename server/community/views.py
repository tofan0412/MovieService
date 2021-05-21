from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Article
from .serializers import ArticleSerializer

@api_view(['GET'])
def articlelist_create(request): 
    if request.method=='GET': 
        articles = Article.objects.all()
        serializer= ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    # else:
    #     serializer = ArticleSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save(user=request.user)
    #         return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def article_update_delete(request, article_pk): 
    article = get_object_or_404(Article, pk=article_pk)
    if request.method=='PUT' : 
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True): 
            serializer.save()
            return Response(serializer.data)
    else:
        article.delete()
        return Response({'id':article_pk}) # 삭제될 때 삭제된 데이터의 id 값을 보여주도록 함.
        

### 댓글 생성 및 삭제 파트 추가