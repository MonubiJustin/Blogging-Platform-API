from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .models import Post, Category, Tag 
from .permissions import IsAuthorOrReadOnly, IsAdmin
from .serializers import PostSerializer, CategorySerializer, TagSerializer, UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdmin]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    
