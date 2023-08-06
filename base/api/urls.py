from django.urls import path
from . import views

# api urls

urlpatterns = [
    path("", views.getRoutes),
    path("rooms/", views.getRooms),
    path("rooms/<str:pk>", views.getRoom),
]
