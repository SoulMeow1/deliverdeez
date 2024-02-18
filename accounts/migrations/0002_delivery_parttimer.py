# Generated by Django 4.2.9 on 2024-02-17 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Delivery",
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
                ("itemName", models.CharField(max_length=200, null=True)),
                ("itemDescription", models.CharField(max_length=200, null=True)),
                ("pickUpLocation", models.CharField(max_length=200, null=True)),
                ("dropOffLocation", models.CharField(max_length=200, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Out for delivery", "Out for delivery"),
                            ("Delivered", "Delivered"),
                        ],
                        max_length=200,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PartTimer",
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
                ("name", models.CharField(max_length=200, null=True)),
                ("phone", models.CharField(max_length=200, null=True)),
                ("email", models.CharField(max_length=200, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
