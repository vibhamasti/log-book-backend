# Generated by Django 3.0.8 on 2020-07-16 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="LogBook",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(max_length=30, verbose_name="subject")),
                (
                    "class_sec",
                    models.CharField(max_length=5, verbose_name="class and section"),
                ),
                ("time_start", models.TimeField(verbose_name="start time")),
                ("time_end", models.TimeField(verbose_name="end time")),
                ("date", models.DateField(verbose_name="date")),
                ("is_substitute", models.BooleanField(default=False)),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "log book entry",
                "verbose_name_plural": "log book entries",
            },
        )
    ]
