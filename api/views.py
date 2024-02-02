import rest_framework_simplejwt
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from api.models import Note, CustomUser
from api.serializers import NoteSerializer, MyTokenObtainPairSerializer, ProfileSerializer, RegisterSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request):
    user = request.user
    serializer = ProfileSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateProfile(request):
    user = request.user
    serializer = ProfileSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    public_notes = Note.objects.order_by('-updated')[:10]
    user_notes = request.user.notes.all().order_by('-updated')[:10]
    notes = user_notes # | public_notes - Для вывода всех записей всех юзеров
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


class NoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = NoteSerializer


class NoteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated, ]
    lookup_field = "pk"
