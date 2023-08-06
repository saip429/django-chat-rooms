from rest_framework.serializers import ModelSerializer
from base.models import Room

# api serializers to convert python object to JSON format


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
