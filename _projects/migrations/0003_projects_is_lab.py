# Generated by Django 5.0.6 on 2024-05-19 00:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("_projects", "0002_projects_links_alter_projects_categories_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="projects",
            name="is_lab",
            field=models.BooleanField(default=False, verbose_name="isLab"),
        ),
    ]