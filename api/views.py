from django.shortcuts import render
from rest_framework import generics, permissions

from api.models import Note
from api.serializers import NoteSerializer


class NoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.DjangoModelPermissions]

class NoteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.DjangoModelPermissions]
    lookup_field = "pk"