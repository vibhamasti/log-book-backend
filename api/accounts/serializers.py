# django imports
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.db.models import Q

# app level imports
from .models import User

# python imports
import logging

logger = logging.getLogger(__name__)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["mobile", "email", "is_staff", "first_name", "last_name"]


class UserRegisterSerializer(serializers.Serializer):
    mobile = serializers.IntegerField(
        min_value=1000000000,
        max_value=9999999999,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    email = serializers.EmailField(
        label=_("Email address"),
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password1 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    first_name = serializers.CharField(max_length=30, required=False)
    last_name = serializers.CharField(max_length=30, required=False)

    def save(self):
        logger.error("inside save serializer")
        user = User(
            mobile=self.validated_data["mobile"], email=self.validated_data["email"]
        )
        password1 = self.validated_data["password1"]
        password2 = self.validated_data["password2"]

        if password1 != password2:
            raise serializers.ValidationError({"password": "Passwords must match."})

        user.set_password(password2)
        user.save()
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    # token = serializers.CharField(allow_blank=True, read_only=True)
    mobile = serializers.IntegerField(min_value=1000000000, max_value=9999999999)
    email = serializers.EmailField(label=_("Email address"))

    class Meta:
        model = User
        fields = ["mobile", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        email = data.get("email", None)
        mobile = data.get("mobile", None)
        password = data.get("password")
        user = None

        if not mobile and not email:
            raise ValidationError("A mobile number or email is required for login.")

        user = User.objects.filter(Q(email=email) | Q(mobile=mobile)).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact="")

        if user.exists() and user.count() == 1:
            user = user.first()
        else:
            raise ValidationError("This mobile number/email is invalid.")

        if user is not None:
            if not user.check_password(password):
                raise ValidationError("Incorrect credentials.")

        # data["token"] = 'my token'

        return data
