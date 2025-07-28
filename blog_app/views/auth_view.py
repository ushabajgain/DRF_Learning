from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
# from serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        return Response({'err': "Username already exists, use another"}, status=status.HTTP_400_BAD_REQUEST)
    try:                    
         User.objects.create_user(
         username=username,
         email=email,
         password=password
    )
         return Response({'msg': "User created successfully"}, status=status.HTTP_200_OK)
    except:
         return Response({'err': "Failed to register User"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username=request.data.get('username')
    password=request.data.get('password')

    if not username:
        return Response({'err':"Username is required"},status=status.HTTP_400_BAD_REQUEST)
    elif not User.objects.filter(username=username).exists():
        return Response({'err':"Invalid Username"},status=status.HTTP_400_BAD_REQUEST)
    
    if not password:
        return Response({'err':"Password is Required"},status=status.HTTP_400_BAD_REQUEST)
    
    user = authenticate(username=username, password=password)
    if user is not None:
        tokens = get_tokens_for_user(user)
        return Response({
            'msg':"User logged in successfully",'tokens': tokens},status=status.HTTP_200_OK)
    else:
        return Response({'err':"Incorrect password"},status=status.HTTP_400_BAD_REQUEST)

