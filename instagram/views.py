from rest_framework import generics
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from rest_framework.views import APIView
from .models import Post

class PublicPostListAPIView(APIView):
    def get(self, request):
        qs = Post.objects.filter(is_public=True)
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)

public_post_list = PublicPostListAPIView.as_view()

# 아래 두개의 url을 해당 값으로 대체 가능 
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
