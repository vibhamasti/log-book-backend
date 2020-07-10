# django imports
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from django.urls import include, path
from django.contrib import admin

# project level imoprts
from accounts.views import UserViewSet

router = DefaultRouter()

router.register(r"accounts/users", UserViewSet, basename="user")

urlpatterns = [
    path("api/", include((router.urls, "api"), namespace="")),
    path("admin/", admin.site.urls),
    path("api-token-auth/", views.obtain_auth_token, name="api-token-auth"),
]
