# Generated by Django 5.0.6 on 2024-05-09 17:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("_links", "0005_links_related_blog_links_related_profile_and_more"),
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
