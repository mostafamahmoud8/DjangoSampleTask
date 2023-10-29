# Generated by Django 4.2 on 2023-10-29 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
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
                ("amount", models.FloatField(verbose_name="transaction amount")),
                (
                    "from_currency",
                    models.CharField(max_length=10, verbose_name="from currency"),
                ),
                (
                    "to_currency",
                    models.CharField(max_length=10, verbose_name="to currency"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("temporary", "Temporary"),
                            ("permanent", "Permanent"),
                        ],
                        default="temporary",
                        max_length=10,
                        verbose_name="transaction status",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_transaction",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
