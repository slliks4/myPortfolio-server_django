# Generated by Django 5.0.6 on 2024-05-09 16:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("_links", "0003_links_url_alter_links_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="links",
            name="related_blog",
        ),
        migrations.RemoveField(
            model_name="links",
            name="related_profile",
        ),
        migrations.RemoveField(
            model_name="links",
            name="related_project",
        ),
    ]
