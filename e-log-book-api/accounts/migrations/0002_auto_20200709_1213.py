# Generated by Django 3.0.8 on 2020-07-09 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("accounts", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(
                default=False,
                help_text="Designates whether the user is a Django User and can log into Django Dashboard",
                verbose_name="staff",
            ),
        )
    ]
