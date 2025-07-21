from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..serializers import StudentSerializer
from ..models import Student

# @api_view(['GET'])
# def index(request):
#     return Response ({'message':"Hello, This is my first API response."})

@api_view(['POST'])
def add_student(request):
    if request.method == 'POST':
       serializer = StudentSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response({'message':"Student Inserted Successfully",'data':serializer.data}, status=status.HTTP_201_CREATED)
       else:
           return Response({'msg':"Failed to insert data"}, status=status.HTTP_400_BAD_REQUEST)
       

@api_view(['GET'])
def get_student(request):
    if request.method == 'GET':
     student = Student.objects.all()
     serializer = StudentSerializer(student, many=True)
    return Response({'data':serializer.data},status=status.HTTP_202_ACCEPTED)


@api_view(['PUT'])
def update_student(request,id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({'msg':"Student not found"})
    
    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Student updated successfully",'data':serializer.data}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'msg':"Failed to update student",'data':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# To get a student id, show the student data of specific id
@api_view(['GET'])
def get_student_by_id(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return Response({'error':"Student not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response({'data':serializer.data}, status=status.HTTP_200_OK)
    
    
@api_view(['DELETE'])
def delete_student(request, id):
    try:
        student = Student.objects.get(id=id)
        # student = get_object_or_404(Student, id=id)
    except Student.DoesNotExist:
        return Response({'msg': "student not found"}, )
    
    student.delete()
    return Response({'msg':'Student delete successfully'},status=status.HTTP_204_NO_CONTENT)
