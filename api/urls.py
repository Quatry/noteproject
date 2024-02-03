from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView

from api.views import NoteListCreateAPIView, NoteRetrieveUpdateDestroyAPIView, MyTokenObtainPairView, RegisterView, \
    ProfileGetPutAPI

urlpatterns = [
    path('notes', NoteListCreateAPIView.as_view(),name='notes_list_create'),
    path('notes/<int:pk>', NoteRetrieveUpdateDestroyAPIView.as_view(),name='note_get_update_delete'),

    path('token', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/logout', TokenBlacklistView.as_view(), name='token_blacklist'),

    path('register', RegisterView.as_view(), name='auth_register'),
    path('profile', ProfileGetPutAPI.as_view(), name='profile_get_put')
]
