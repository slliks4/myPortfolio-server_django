# Generated by Django 5.0.6 on 2024-06-01 23:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("_blogs", "0003_blogs_links_alter_blogs_related_projects"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blogs",
            options={
                "ordering": ("-id",),
                "verbose_name": "Blogs",
                "verbose_name_plural": "Blogs",
            },
        ),
    ]
