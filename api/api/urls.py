# django imports
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from django.urls import include, path
from django.contrib import admin

# project level imports
from accounts.views import UserViewSet, UserLoginViewSet, UserRegisterViewSet

router = DefaultRouter()

router.register(r"accounts/users", UserViewSet, basename="user")
router.register(r"accounts", UserRegisterViewSet, basename="register")
router.register(r"accounts", UserLoginViewSet, basename="login")

urlpatterns = [
    path("api/", include((router.urls, "api"), namespace="")),
    path("admin/", admin.site.urls),
    path("api-token-auth/", views.obtain_auth_token, name="api-token-auth"),
]
