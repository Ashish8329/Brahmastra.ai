# Generated by Django 5.1.3 on 2024-11-22 07:51

import user.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_remove_customuser_unique_email"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="customuser",
            managers=[
                ("objects", user.models.CustomUserManager()),
            ],
        ),
    ]
