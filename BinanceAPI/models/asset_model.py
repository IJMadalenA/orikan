from django.db.models import (
    CharField,
    TextField
)

from BinanceAPI.models.base_binance_model import BaseBinanceModel


class Asset(BaseBinanceModel):
    symbol = CharField(
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
    status = CharField(
        max_length=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Estado del par de trading",
    )

    class Meta:
        db_table = 'assets'

    def __str__(self):
        return self.symbol
