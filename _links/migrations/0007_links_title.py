# Generated by Django 5.0.6 on 2024-06-14 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_links', '0006_remove_links_related_blog_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='title',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Name'),
        ),
    ]