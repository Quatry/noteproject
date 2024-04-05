from django.urls import path

from api.views import NoteListCreateAPIView, NoteRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('notes', NoteListCreateAPIView.as_view(),name='notes_list_create'),
    path('notes/<int:pk>', NoteRetrieveUpdateDestroyAPIView.as_view(),name='note_get_update_delete'),
]
