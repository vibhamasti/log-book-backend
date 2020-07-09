# django imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# app level imports
from .models import User
from .forms import UserChangeForm, UserCreationForm


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = (
        "mobile",
        "email",
        "first_name",
        "last_name",
        "date_joined",
        "is_active",
        "is_staff",
    )
    list_filter = ("is_active",)

    search_fields = ()
    ordering = ()

    fieldsets = (
        (None, {"fields": ("mobile", "email", "password", "first_name", "last_name")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "mobile",
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "first_name",
                    "last_name",
                ),
            },
        ),
    )
