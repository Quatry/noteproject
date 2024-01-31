from django.urls import path

from api.views import NoteListCreateAPIView, NoteRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('',NoteListCreateAPIView.as_view()),
    path('<int:pk>',NoteRetrieveUpdateDestroyAPIView.as_view()),
]