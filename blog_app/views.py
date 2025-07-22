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

from rest_framework.decorators import api_view # for function based view
from rest_framework.views import APIView # for class based view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer

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
        


