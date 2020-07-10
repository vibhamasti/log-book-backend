from django.shortcuts import render  # noqa
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
