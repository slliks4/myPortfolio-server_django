# Generated by Django 5.0.6 on 2024-05-09 16:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("_blogs", "0003_blogs_links_alter_blogs_related_projects"),
        ("_links", "0004_remove_links_related_blog_and_more"),
        ("_profile", "0002_alter_tel_options"),
        ("_projects", "0002_projects_links_alter_projects_categories_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="links",
            name="related_blog",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="blogs",
                to="_blogs.blogs",
            ),
        ),
        migrations.AddField(
            model_name="links",
            name="related_profile",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="profile",
                to="_profile.profile",
            ),
        ),
        migrations.AddField(
            model_name="links",
            name="related_project",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="projects",
                to="_projects.projects",
            ),
        ),
    ]
