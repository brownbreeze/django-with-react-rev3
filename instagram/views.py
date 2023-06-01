from rest_framework import generics
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post


class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# 아래 두개의 url을 해당 값으로 대체 가능 
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer   

    def dispatch(self, request, *args, **kwargs):
        # print() 비추
        print("request.body: ", request.body)
        print("request.POST: ", request.POST)
        return super().dispatch(request, *args, **kwargs)

# def post_list(request):
#     #최소 두개 분리 
#     pass
# def post_detail(request, pk):
#     #최소 세개 분기 
#     pass