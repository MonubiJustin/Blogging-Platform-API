from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Post, Category, Tag

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]
        
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag 
        fields = ["name"]
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username", "email")
        
        

