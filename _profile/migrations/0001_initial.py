# Generated by Django 5.0.6 on 2024-05-09 16:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("_links", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_name", models.CharField(max_length=50, verbose_name="username")),
                (
                    "first_name",
                    models.CharField(max_length=100, verbose_name="First name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=150, verbose_name="Last name"),
                ),
                (
                    "pic",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="uploads/_profile/images",
                        verbose_name="Profile picture",
                    ),
                ),
                ("address", models.TextField()),
                (
                    "home_text",
                    models.CharField(max_length=50, verbose_name="Home text"),
                ),
                (
                    "files",
                    models.FileField(
                        upload_to="uploads/_profile/files", verbose_name="Files"
                    ),
                ),
                ("links", models.ManyToManyField(blank=True, to="_links.links")),
            ],
            options={
                "verbose_name": "Profile",
                "verbose_name_plural": "Profile",
                "db_table": "Profile",
            },
        ),
        migrations.CreateModel(
            name="Experience",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=450, verbose_name="Title")),
                (
                    "date_period",
                    models.CharField(max_length=350, verbose_name="Date Period"),
                ),
                (
                    "company_name",
                    models.CharField(max_length=450, verbose_name="Company Name"),
                ),
                (
                    "company_link",
                    models.CharField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="Company Link",
                    ),
                ),
                ("text", models.TextField(verbose_name="Text")),
                (
                    "profile",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="experience",
                        to="_profile.profile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Experience",
                "verbose_name_plural": "Experience",
                "db_table": "Experience",
            },
        ),
        migrations.CreateModel(
            name="Email",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                (
                    "profile",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="email",
                        to="_profile.profile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Email",
                "verbose_name_plural": "Email",
                "db_table": "Email",
            },
        ),
        migrations.CreateModel(
            name="Education",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "degree",
                    models.CharField(max_length=450, verbose_name="Degree name"),
                ),
                (
                    "date_period",
                    models.CharField(max_length=350, verbose_name="Date Period"),
                ),
                (
                    "school_name",
                    models.CharField(max_length=450, verbose_name="School Name"),
                ),
                (
                    "school_link",
                    models.CharField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="School Link",
                    ),
                ),
                ("text", models.TextField(verbose_name="Text")),
                (
                    "profile",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="education",
                        to="_profile.profile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Education",
                "verbose_name_plural": "Education",
                "db_table": "Education",
            },
        ),
        migrations.CreateModel(
            name="Services",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150, verbose_name="Title")),
                ("text", models.TextField(verbose_name="Text")),
                (
                    "icon",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="uploads/_profile/icons",
                        verbose_name="Icon",
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                (
                    "profile",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="service",
                        to="_profile.profile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Services",
                "verbose_name_plural": "Services",
                "db_table": "Services",
            },
        ),
        migrations.CreateModel(
            name="Tel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tel", models.CharField(max_length=14, verbose_name="Tel")),
                (
                    "profile",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="tel",
                        to="_profile.profile",
                    ),
                ),
            ],
            options={
                "verbose_name": "",
                "verbose_name_plural": "",
                "db_table": "Tel",
            },
        ),
    ]
