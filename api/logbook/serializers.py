# django imports
from rest_framework import serializers

# app level imports
from .models import LogBook


class LogBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogBook
        fields = "__all__"
