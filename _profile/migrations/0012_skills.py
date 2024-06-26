# Generated by Django 5.0.6 on 2024-05-21 08:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("_profile", "0011_alter_profile_mission_alter_profile_vision"),
    ]

    operations = [
        migrations.CreateModel(
            name="Skills",
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
                ("name", models.CharField(max_length=150, verbose_name="name")),
                ("level", models.CharField(max_length=150, verbose_name="level")),
                (
                    "profile",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="skills",
                        to="_profile.profile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Skills",
                "verbose_name_plural": "Skills",
                "db_table": "Skills",
            },
        ),
    ]
