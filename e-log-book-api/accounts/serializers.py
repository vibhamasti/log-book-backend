# django imports
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

# app level imports
from .models import User


class UserSerializer(serializers.ModelSerializer):
    # mobile = serializers.IntegerField(min_value=1000000000, max_value=9999999999)

    class Meta:
        model = User
        fields = ["mobile", "email", "is_staff", "first_name", "last_name"]

        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(), fields=["mobile", "email"]
            )
        ]
