# python imports
import logging

# django imports
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate

# app level imports
from .models import User


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


class UserLoginSerializer(serializers.Serializer):
    mobile = serializers.IntegerField(
        label=_("Mobile"), min_value=1000000000, max_value=9999999999
    )
    password = serializers.CharField(
        label=_("Password"), style={"input_type": "password"}, trim_whitespace=False
    )

    def validate(self, attrs):
        mobile = attrs.get("mobile")
        password = attrs.get("password")

        if mobile and password:
            user = authenticate(
                request=self.context.get("request"), username=mobile, password=password
            )

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _("Unable to log in with provided credentials.")
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = _('Must include "mobile" and "password".')
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs
