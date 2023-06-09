from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post

@api_view(['GET'])
def public_post_list(request):
    qs = Post.objects.filter(is_public=True)
    serializer = PostSerializer(qs, many=True)
    return Response(serializer.data)

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
