from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data.get('username'))
    if not user.check_password(request.data.get('password')):
        return Response("Invalid credentials", status=status.HTTP_401_UNAUTHORIZED)

    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.create_user(
            username=request.data.get('username'),
            password=request.data.get('password')
        )
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    # Delete the user's token to log them out
    request.auth.delete()
    return Response({"detail": "Logout successful"}, status=200)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed!")