# django imports
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

# app level imports
from .models import User
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]


class UserRegisterViewSet(viewsets.GenericViewSet):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    @action(methods=["POST"], detail=False, url_path="")
    def register(self, request):
        if request.method == "POST":
            serializer = self.serializer_class(data=request.data)
            data = {}

            if serializer.is_valid():
                user = serializer.save()
                data["response"] = "Successfully created new user"
                data["mobile"] = user.mobile
                data["email"] = user.email
            else:
                data = serializer.errors
        else:
            data = {}
        return Response(data)


class UserLoginViewSet(viewsets.GenericViewSet):
    """ A viewset for logging users in. """

    serializer_class = UserLoginSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    @action(methods=["POST"], detail=False, url_path="")
    def login(self, request):
        if request.method == "POST":
            serializer = UserLoginSerializer(data=request.data)
            data = {}

            if serializer.is_valid():
                user = serializer.save()
                data["response"] = "Successfully created new user"
                data["mobile"] = user.mobile
                data["email"] = user.email
            else:
                data = serializer.errors
        else:
            data = {}
        return Response(data)
