from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from api.models import Note
from api.serializers import NoteSerializer






class NoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def list(self, request):
        public_notes = Note.objects.order_by('-updated')[:10]
        serializer = NoteSerializer(public_notes, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = {
            "body": request.data['body'],        }
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class NoteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = "pk"
