from rest_framework import generics
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post

class PublicPostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# 아래 두개의 url을 해당 값으로 대체 가능 
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer   

# def post_list(request):
#     pass 

# post_list = csrf_exempt(post_list) # 고차 컴포넌트 (higher order component)