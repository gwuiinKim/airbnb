from django.urls import path
from . import views

app_name = "rooms"

#                     argument
# urlpatterns = [path("<int:pk>", views.room_detail, name="detail")]
urlpatterns = [
    path("<int:pk>/", views.RoomDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", views.EditRoom.as_view(), name="edit"),
    path("<int:pk>/photos/", views.RoomPhtos.as_view(), name="photos"),


    path("search/", views.search, name="search")
]
