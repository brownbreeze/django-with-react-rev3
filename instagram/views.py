from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post

# 아래 두개의 url을 해당 값으로 대체 가능 
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer    

# def post_list(request):
#     #최소 두개 분리 
#     pass
# def post_detail(request, pk):
#     #최소 세개 분기 
#     pass