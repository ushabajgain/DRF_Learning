from rest_framework import serializers
from .models import Blog, Category, Product
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
    category_title = serializers.CharField(source='category.title', read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'title','price', 'description', 'category', 'user', 'created_at', 'updated_at', 'category_title']
        read_only_fields = ['id', 'user', 'created_at', 'category_title']        

class CategoryWithProductsSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True, source='product_set')
    class Meta:
        model = Category
        fields = ['id', 'title', 'products']        

        