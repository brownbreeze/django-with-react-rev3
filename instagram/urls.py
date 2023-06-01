from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet) # 두개의 URL 을 생성 
# router.urls # pattern list 

urlpatterns = [
    path('public/', views.PostListAPIView.as_view()),
    path('', include(router.urls)),
]