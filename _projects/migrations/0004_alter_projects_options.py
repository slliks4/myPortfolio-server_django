# Generated by Django 5.0.6 on 2024-06-01 23:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("_projects", "0003_projects_is_lab"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="projects",
            options={
                "ordering": ("-id",),
                "verbose_name": "Projects",
                "verbose_name_plural": "Projects",
            },
        ),
    ]
