# Generated by Django 4.1.5 on 2023-01-26 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CnabTransactions",
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
                ("type", models.CharField(max_length=1)),
                ("date", models.DateField(max_length=8)),
                (
                    "value",
                    models.DecimalField(decimal_places=2, max_digits=10, max_length=10),
                ),
                ("cpf", models.CharField(max_length=11)),
                ("card", models.CharField(max_length=12)),
                ("hour", models.DateTimeField(max_length=6)),
                ("store_owner", models.CharField(max_length=14)),
                ("store_name", models.CharField(max_length=19)),
            ],
            options={
                "ordering": ("id",),
            },
        ),
    ]