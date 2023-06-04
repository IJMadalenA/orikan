from django.db.models import (
    CharField,
    DateTimeField,
    DecimalField,
    IntegerField,
)

from BinanceAPI.models.base_binance_model import BaseBinanceModel


class Deposit(BaseBinanceModel):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    )

    deposit_id = CharField(
        max_length=100,
        unique=True,
        blank=False,
        null=False,
        editable=False,
        help_text="ID de depósito"
    )
    amount = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Cantidad depositada"
    )
    asset = CharField(
        max_length=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Activo"
    )
    address = CharField(
        max_length=100,
        blank=False,
        null=False,
        editable=False,
        help_text="Dirección de depósito"
    )
    tx_id = CharField(
        max_length=100,
        null=True,
        blank=True,
        editable=False,
        help_text="ID de transacción"
    )
    status = CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        blank=False,
        null=False,
        editable=False,
        help_text="Estado del depósito"
    )
    timestamp = DateTimeField(
        blank=False,
        null=False,
        editable=False,
        help_text="Fecha y hora del depósito"
    )
    confirmations = IntegerField(
        null=True,
        blank=True,
        editable=False,
        help_text="Número de confirmaciones"
    )
    fee = DecimalField(
        max_digits=20,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="Tarifa de depósito"
    )
    tx_hash = CharField(
        max_length=100,
        null=True,
        blank=True,
        editable=False,
        help_text="Hash de la transacción"
    )

    class Meta:
        db_table = 'deposits'

    def __str__(self):
        return f"Deposit ID: {self.deposit_id}, Amount: {self.amount}, Asset: {self.asset}, Status: {self.status}"