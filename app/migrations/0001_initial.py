# Generated by Django 4.1.2 on 2022-10-23 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserPage",
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
                    "avatar",
                    models.ImageField(
                        upload_to="users_image", verbose_name="User image"
                    ),
                ),
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                (
                    "is_auth",
                    models.CharField(
                        choices=[
                            ("Admin", "Admin"),
                            ("Member", "Member"),
                            ("Registered", "Registered"),
                        ],
                        default="Registered",
                        max_length=15,
                    ),
                ),
                ("birth_date", models.DateField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Inactive", "Inactive"),
                            ("Active", "Active"),
                            ("Banned", "Banned"),
                            ("Pending", "Pending"),
                        ],
                        default="Banned",
                        max_length=15,
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]