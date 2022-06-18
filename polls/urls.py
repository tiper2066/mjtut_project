from django.urls import path
from . import views     # views.py의 모든걸 가져옴

urlpatterns = [
    path('', views.index, name = 'index')  # 홈경로, namespace = index 설정
]
