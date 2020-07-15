# django imports
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

# app level imports
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    mobile = models.BigIntegerField(
        _("mobile"),
        unique=True,
        validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)],
    )
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(_("first name"), max_length=30, blank=True)
    last_name = models.CharField(_("last name"), max_length=30, blank=True)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    is_active = models.BooleanField(_("active"), default=True)
    is_staff = models.BooleanField(
        _("staff"),
        default=False,
        help_text=_(
            "Designates whether the user is a Django User and can log into Django Dashboard"
        ),
    )
    is_superuser = models.BooleanField(_("superuser"), default=False)
    # avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "mobile"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = "user"

    def get_mobile(self):
        """
        Returns the user's mobile number
        """
        return self.mobile

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def __str__(self):
        return str(self.mobile)
