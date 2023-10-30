# Generated by Django 4.2 on 2023-10-29 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0003_transaction_result_alter_transaction_exhange_rate"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExchangeRate",
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
                    "from_currency",
                    models.CharField(max_length=10, verbose_name="from currency"),
                ),
                (
                    "to_currency",
                    models.CharField(max_length=10, verbose_name="to currency"),
                ),
                ("rate", models.FloatField(verbose_name="currency exchange rate")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        )
    ]
