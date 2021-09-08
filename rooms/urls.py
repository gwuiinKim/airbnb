from django.urls import path
from . import views

app_name = "rooms"

#                     argument
urlpatterns = [path("<int:pk>", views.room_detail, name="detail")]