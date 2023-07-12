from django.db.models import (
    CharField,
    TextField,
    DecimalField,
    BooleanField
)
from BinanceAPI.models.base_binance_model import BaseBinanceModel


class Asset(BaseBinanceModel):
    acronym = CharField(
        db_index=True,
        max_length=20,
        unique=True,
        blank=False,
        null=False,
        editable=False,
        help_text="Símbolo del par de trading",
    )
    name = CharField(
        max_length=20,
        blank=True,
        null=True,
        editable=True,
        help_text="Nombre del activo.",
    )
    description = TextField(
        blank=True,
        null=True,
        editable=True,
        help_text="Descripción del activo.",
    )
    min_withdraw_amount = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=True,
        help_text="Cantidad mínima para retirar.",
    )
    deposit_status = BooleanField(
        blank=False,
        null=False,
        editable=True,
        help_text="Estado de depósito.",
    )
    withdraw_fee = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=True,
        help_text="Comisión de retiro.",
    )
    withdraw_status = BooleanField(
        blank=False,
        null=False,
        editable=True,
        help_text="Estado de retiro.",
    )
    deposit_tip = TextField(
        blank=True,
        null=True,
        editable=True,
        help_text="Consejo de depósito.",
    )

    class Meta:
        db_table = 'assets'

    def __str__(self):
        return self.acronym
