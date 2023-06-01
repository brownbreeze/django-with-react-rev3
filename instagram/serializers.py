from rest_framework.serializers import ModelSerializer
from .models import Post
from rest_framework import serializers
from django.contrib.auth import get_user_model

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']
        fields = [' user name ' ]

class PostSerializer(serializers.ModelSerializer):
    author_email = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = [
            'pk',
            'author_email',
            'message',
            'created_at',
            'updated_at',
        ] 