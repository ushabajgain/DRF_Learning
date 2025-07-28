#-----Function-Based View-----#

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Blog
# from .serializers import BlogSerializer

# @api_view(['POST', 'GET'])
# # For 'POST' Request
# def blog_view(request):
#     if request.method == 'POST':
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': "Blog inserted successfully."}, status=status.HTTP_201_CREATED)
#         return Response({'msg': "Failed to insert blog.", 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# # For 'GET' Request
#     elif request.method == 'GET':
#         blogs = Blog.objects.all()  
#         serializer = BlogSerializer(blogs, many=True)  
#         return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    

# @api_view(['PUT', 'DELETE', 'GET'])
# # For 'PUT' Request
# def blog_update(request,id):
#     try:
#         blogs = Blog.objects.get(id=id)
#     except Blog.DoesNotExist:
#         return Response({'msg':"Blog not found"},status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'PUT':
#         serializer = BlogSerializer(blogs, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':"Blog updated successfully",'data':serializer.data}, status=status.HTTP_202_ACCEPTED)
#         else:
#             return Response({'msg':"Failed to update blog",'data':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
# # For 'DELETE' Request    
#     elif request.method == 'DELETE':
#         blogs.delete()
#         return Response({'msg':'Blog delete successfully'},status=status.HTTP_204_NO_CONTENT)

# # For "GET_BY_ID" Request
#     elif request.method == 'GET':
#         blogs = Blog.objects.get(id=id)
#         serializer = BlogSerializer(blogs)
#         return Response({'data':serializer.data},status=status.HTTP_200_OK)


#-----Class-Based View-----#

# from rest_framework.decorators import api_view, permission_classes # for function based view
# from rest_framework.views import APIView # for class based view
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.response import Response
# from rest_framework import status
# from blog_app.models import Blog, Category
# from blog_app.serializers import BlogSerializer
# from blog_app.serializers import CategorySerializer

# blog_app/views/auth_view.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from blog_app.models import Blog, Category
from blog_app.serializers import BlogSerializer, CategorySerializer


class BlogView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id=None):
        if id is not None:
            try:
                blog = Blog.objects.get(id=id)
                serializer = BlogSerializer(blog)
                return Response({'data': serializer.data}, status=status.HTTP_200_OK)
            except Blog.DoesNotExist:
                return Response({'msg': "Blog not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            blog = Blog.objects.all()
            serializer = BlogSerializer(blog, many=True)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Blog posted Successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({'msg': "Failed to post blog", 'err': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, id=None):
        if id is None:
            return Response({'msg': "Blog id is required for update"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            blog = Blog.objects.get(id=id)
        except Blog.DoesNotExist:
            return Response({'msg': "Blog not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Blog updated successfully", 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'msg': "Failed to update blog", 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id=None):
        if id is None:
            return Response({'msg': "Blog id is required for delete"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            blog = Blog.objects.get(id=id)
            blog.delete()
            return Response({'msg': 'Blog deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Blog.DoesNotExist:
            return Response({'msg': "Blog not found"}, status=status.HTTP_404_NOT_FOUND)
        

@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def category_view(request):
    if request.method == 'POST':
      serializer = CategorySerializer(data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response({'msg':"Category added successfully"},status=status.HTTP_201_CREATED)
      else:
          return Response({'msg':"Failed to add category",'err':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
      

    if request.method == 'GET':
        category= Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)    
    

@api_view(['PUT', 'DELETE', 'GET'])
@permission_classes([IsAuthenticated])
def category_update(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response({'msg': "Category not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Category updated successfully", 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'msg': "Failed to update category", 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response({'msg': 'Category deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
