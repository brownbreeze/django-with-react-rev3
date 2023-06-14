from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

# 2개의 URL을 만들어 줌. router를 이용해 일괄적 등록 가능 
# 아래 방식을 추천 
router = DefaultRouter()
router.register('post', views.PostViewSet)

urlpatterns = [
    path('mypost/<int:pk>/', views.PostDetailAPIView.as_view()),
    path('public/', views.public_post_list),
    path('', include(router.urls)),
]