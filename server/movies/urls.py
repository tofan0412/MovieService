from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('detail/<int:movie_pk>/', views.detail),
    path('detail/<int:movie_id>/rate_list_create/', views.rate_list_create),
    path('detail/<int:rate_pk>/rate_delete/', views.rate_delete),
    path('detail/<int:movie_pk>/rate_update/', views.rate_update),
]