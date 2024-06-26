# Generated by Django 5.0.6 on 2024-05-09 17:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("_profile", "0003_alter_profile_home_text"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="files",
        ),
        migrations.CreateModel(
            name="Files",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="uploads/_profile/files",
                        verbose_name="Files",
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="files",
                        to="_profile.profile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Files",
                "verbose_name_plural": "Files",
                "db_table": "Files",
            },
        ),
    ]
