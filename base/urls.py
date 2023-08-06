# urls for base app
from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerUser, name="register"),
    path("", views.home, name="home"),
    path(
        "room/<str:pk>/", views.room, name="room"
    ),  # <> dynamic value where str: string and pk: primary key
    path("profile/<str:pk>", views.userProfile, name="user-profile"),
    path("create-room/", views.createRoom, name="create-room"),
    path("update-room/<str:pk>/", views.updateRoom, name="update-room"),
    path("delete-room/<str:pk>", views.deleteRoom, name="delete-room"),
    path(
        "delete-message/<str:pk>/<str:sk>", views.deleteMessage, name="delete-message"
    ),
    path("update-user/", views.updateUser, name="update-user"),
    path("topics/", views.topicsPage, name="topics"),
    path("activity", views.activities, name="activity"),
]
