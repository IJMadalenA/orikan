from django.db.models import (
    CharField,
    IntegerField,
)

from BinanceAPI.models.base_binance_model import BaseBinanceModel


class Symbol(BaseBinanceModel):
    symbol = CharField(
        max_length=20,
        unique=True,
        blank=False,
        null=False,
        editable=False,
        help_text="Símbolo del par de trading",
    )
    base_asset = CharField(
        max_length=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Activo base",
    )
    quote_asset = CharField(
        max_length=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Activo de cotización",
    )
    status = CharField(
        max_length=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Estado del par de trading",
    )
    base_asset_precision = IntegerField(
        blank=False,
        null=False,
        editable=False,
        help_text="Precisión del activo base",
    )
    quote_asset_precision = IntegerField(
        blank=False,
        null=False,
        editable=False,
        help_text="Precisión del activo de cotización",
    )

    class Meta:
        db_table = 'symbols'

    def __str__(self):
        return self.symbol
