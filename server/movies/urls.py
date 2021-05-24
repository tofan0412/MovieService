from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('detail/<int:movie_pk>/', views.detail),
    path('detail/<int:movie_pk>/trailer/', views.trailer),
    path('detail/<int:movie_pk>/review_list/', views.review_list),
    path('detail/<int:movie_pk>/review_list_create/', views.review_list_create),
    path('detail/<int:review_pk>/review_delete/', views.review_delete),
    path('detail/<int:review_pk>/review_update/', views.review_update),
    path('detail/<int:review_pk>/like/', views.like),
] 