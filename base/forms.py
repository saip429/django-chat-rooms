# model form
from django.forms import ModelForm

from .models import Room, User
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class RoomForm(ModelForm):
    class Meta:  # metadata
        model = Room
        fields = "__all__"  # fields based on model
        exclude = ["host", "participants"]


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["avatar", "username", "email", "bio"]
