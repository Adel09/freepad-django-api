from rest_framework import serializers
from .models import PadRequest

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PadRequest
        fields = "__all__"