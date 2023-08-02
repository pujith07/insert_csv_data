# Generated by Django 4.1.7 on 2023-06-16 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bank",
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
                ("NAME", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Branch",
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
                ("IFSC", models.CharField(max_length=100)),
                ("BRANCH", models.CharField(max_length=100)),
                ("ADDRESS", models.TextField()),
                ("CONTACT", models.IntegerField()),
                ("CITY", models.CharField(max_length=100)),
                ("DISTRICT", models.CharField(max_length=100)),
                ("STATE", models.CharField(max_length=100)),
                (
                    "NAME",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.bank"
                    ),
                ),
            ],
        ),
    ]
