# Generated by Django 5.0.6 on 2024-05-09 16:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("_profile", "0002_alter_tel_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="home_text",
            field=models.CharField(max_length=500, verbose_name="Home text"),
        ),
    ]
