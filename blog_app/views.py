from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer

@api_view(['POST', 'GET'])
def blog_view(request):
    if request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Blog inserted successfully."}, status=status.HTTP_201_CREATED)
        return Response({'msg': "Failed to insert blog.", 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        blogs = Blog.objects.all()  
        serializer = BlogSerializer(blogs, many=True)  
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    

@api_view(['PUT', 'DELETE', 'GET'])
def blog_update(request,id):
    try:
        blogs = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        return Response({'msg':"Blog not found"},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = BlogSerializer(blogs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Blog updated successfully",'data':serializer.data}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'msg':"Failed to update blog",'data':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        blogs.delete()
        return Response({'msg':'Student delete successfully'},status=status.HTTP_204_NO_CONTENT)


    elif request.method == 'GET':
        blogs = Blog.objects.get(id=id)
        serializer = BlogSerializer(blogs)
        return Response({'data':serializer.data},status=status.HTTP_200_OK)

