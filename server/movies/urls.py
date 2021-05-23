from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('detail/<int:movie_pk>/', views.detail),
    path('detail/<int:movie_id>/rank_list_create/', views.rank_list_create),
    path('detail/<int:rank_pk>/rank_delete/', views.rank_delete),
    path('detail/<int:movie_pk>/rank_update/', views.rank_update),
    # 좋아요 추가 예정
] 