# Generated by Django 4.2.15 on 2024-08-17 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Question",
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
                ("text", models.TextField()),
                ("difficulty", models.CharField(max_length=10)),
                ("options", models.JSONField()),
                ("correct_answer", models.CharField(max_length=255)),
                (
                    "pdf",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.pdf"
                    ),
                ),
            ],
        ),
    ]
