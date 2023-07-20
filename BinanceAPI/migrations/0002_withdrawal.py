# Generated by Django 4.2.1 on 2023-07-20 07:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("BinanceAPI", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Withdrawal",
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
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, help_text="Fecha y hora de actualización"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, help_text="Fecha y hora de creación"
                    ),
                ),
                (
                    "withdrawal_id",
                    models.CharField(
                        db_index=True,
                        editable=False,
                        help_text="ID de retiro",
                        max_length=100,
                        unique=True,
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=10,
                        editable=False,
                        help_text="Cantidad retirada",
                        max_digits=20,
                    ),
                ),
                (
                    "asset",
                    models.CharField(editable=False, help_text="Activo", max_length=10),
                ),
                (
                    "address",
                    models.CharField(
                        editable=False, help_text="Dirección de retiro", max_length=100
                    ),
                ),
                (
                    "tx_id",
                    models.CharField(
                        blank=True,
                        editable=False,
                        help_text="ID de transacción",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("success", "Success"),
                            ("failed", "Failed"),
                        ],
                        editable=False,
                        help_text="Estado del retiro",
                        max_length=10,
                    ),
                ),
                (
                    "timestamp",
                    models.DateTimeField(
                        editable=False, help_text="Fecha y hora del retiro"
                    ),
                ),
                (
                    "fee",
                    models.DecimalField(
                        blank=True,
                        decimal_places=10,
                        editable=False,
                        help_text="Tarifa de retiro",
                        max_digits=20,
                        null=True,
                    ),
                ),
                (
                    "tx_hash",
                    models.CharField(
                        blank=True,
                        editable=False,
                        help_text="Hash de la transacción",
                        max_length=100,
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "withdrawal",
                "verbose_name_plural": "withdrawals",
                "ordering": ["-timestamp"],
            },
        ),
    ]
