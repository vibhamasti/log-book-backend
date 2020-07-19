# django imports
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema
from rest_framework import status

# app level imports
from .models import User
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer

# python imports
import logging

logger = logging.getLogger(__name__)


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]


class UserRegisterViewSet(viewsets.GenericViewSet):
    """
    A viewset for registering users.
    """

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
                token = Token.objects.get(user=user).key
                data["token"] = token
                req_status = status.HTTP_201_CREATED
            else:
                data = serializer.errors
                req_status = status.HTTP_400_BAD_REQUEST
        else:
            data = {}
            req_status = status.HTTP_403_FORBIDDEN
        return Response(data, status=req_status)


class UserLoginViewSet(viewsets.GenericViewSet, ObtainAuthToken):
    """
    A viewset for logging users in.
    """

    serializer_class = UserLoginSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    if coreapi is not None and coreschema is not None:
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="mobile",
                    required=True,
                    location="form",
                    schema=coreschema.String(
                        title="Mobile", description="Valid mobile for authentication"
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location="form",
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    @action(methods=["POST"], detail=False, url_path="")
    def login(self, request):
        if request.method == "POST":
            serializer = self.serializer_class(
                data=request.data, context={"request": request}
            )
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data["user"]
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
