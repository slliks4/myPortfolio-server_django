# Generated by Django 5.0.6 on 2024-06-19 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_blogs', '0004_alter_blogs_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='_blogs/images'),
        ),
    ]