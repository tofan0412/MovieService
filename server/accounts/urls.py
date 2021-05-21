from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup),
    # 토큰 파트 추가
]