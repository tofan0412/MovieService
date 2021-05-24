from django.urls import path
from . import views


urlpatterns = [
    path('', views.article_list),
    path('articlelist_create/', views.articlelist_create),
    path('<int:article_pk>/article_update_delete/', views.article_update_delete),
    path('<int:article_pk>/comment_list/', views.comment_list),
    path('<int:article_pk>/comment_list_create/', views.comment_list_create),
    path('<int:comment_pk>/comment_delete/', views.comment_delete),
]