# django imports
from django.contrib import admin

# app level imports
from .models import LogBook


@admin.register(LogBook)
class LogBookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "teacher",
        "subject",
        "log_class",
        "log_section",
        "time_start",
        "time_end",
        "date",
        "is_substitute",
    )
