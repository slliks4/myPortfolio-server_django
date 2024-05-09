# Generated by Django 5.0.6 on 2024-05-09 17:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("_profile", "0005_profile_about_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="services",
            name="profile",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="services",
                to="_profile.profile",
            ),
        ),
    ]
