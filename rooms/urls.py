from django.urls import path

from .views import RoomListView, RoomDetail

urlpatterns = [
    path("<int:pk>/", RoomDetail.as_view(), name="room_detail"),
    path("", RoomListView.as_view(), name="room_list"),
]