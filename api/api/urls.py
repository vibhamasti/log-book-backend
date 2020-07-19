# django imports
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from django.contrib import admin

# project level imports
from accounts.views import UserViewSet, UserLoginViewSet, UserRegisterViewSet
from logbook.views import LogBookViewSet

router = DefaultRouter()

router.register(r"accounts/users", UserViewSet, basename="user")
router.register(r"logbook", LogBookViewSet, base_name="logbook")
router.register(r"accounts", UserRegisterViewSet, basename="register")
router.register(r"accounts", UserLoginViewSet, basename="login")

urlpatterns = [
    path("api/", include((router.urls, "api"), namespace="")),
    path("admin/", admin.site.urls),
]
