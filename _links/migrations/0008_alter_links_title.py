# Generated by Django 5.0.6 on 2024-06-14 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_links', '0007_links_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='title',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Title'),
        ),
    ]
