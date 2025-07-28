from rest_framework import serializers
from .models import Blog, Category, product
from django.contrib.auth.models import User

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ['id', 'title','price', 'description', 'category', 'user', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']        