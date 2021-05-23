from django.urls import path
from . import views


urlpatterns = [
    path('', views.articlelist_create),
    path('<int:article_pk>/', views.article_update_delete),
    # 댓글 생성 및 댓글 삭제 추가 예정
]