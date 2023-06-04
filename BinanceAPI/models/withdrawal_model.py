from django.db.models import (
    CharField,
    DateTimeField,
    DecimalField,
)

from BinanceAPI.models.base_binance_model import BaseBinanceModel


class Withdrawal(BaseBinanceModel):
    """
    Este modelo almacena la información sobre las retiradas realizadas desde la cuenta.
    """
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    )

    withdrawal_id = CharField(
        db_index=True,
        max_length=100,
        unique=True,
        blank=False,
        null=False,
        editable=False,
        help_text="ID de retiro",
    )
    amount = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Cantidad retirada",
    )
    asset = CharField(
        max_length=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Activo",
    )
    address = CharField(
        max_length=100,
        blank=False,
        null=False,
        editable=False,
        help_text="Dirección de retiro",
    )
    tx_id = CharField(
        max_length=100,
        null=True,
        blank=True,
        editable=False,
        help_text="ID de transacción",
    )
    status = CharField(
        max_length=10,
        blank=False,
        null=False,
        editable=False,
        choices=STATUS_CHOICES,
        help_text="Estado del retiro",
    )
    timestamp = DateTimeField(
        blank=False,
        null=False,
        editable=False,
        help_text="Fecha y hora del retiro",
    )
    fee = DecimalField(
        max_digits=20,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="Tarifa de retiro",
    )
    tx_hash = CharField(
        max_length=100,
        null=True,
        blank=True,
        editable=False,
        help_text="Hash de la transacción",
    )

    class Meta:
        db_table = 'withdrawals'

    def __str__(self):
        return f"Withdrawal ID: {self.withdrawal_id}, Amount: {self.amount}, Asset: {self.asset}, Status: {self.status}"