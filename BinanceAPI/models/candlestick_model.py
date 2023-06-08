from django.db.models import (
    ForeignKey,
    DateTimeField,
    DecimalField,
    CASCADE
)

from BinanceAPI.models.base_binance_model import BaseBinanceModel
from BinanceAPI.models.symbol_model import Symbol


class Candlestick(BaseBinanceModel):
    symbol = ForeignKey(
        Symbol,
        on_delete=CASCADE,
        related_name='candlesticks',
        null=True,
        blank=True,
        editable=False,
        help_text="Símbolo del par de trading"
    )
    open_time = DateTimeField(
        null=True,
        blank=True,
        editable=False,
        help_text="Fecha y hora de apertura de la vela"
    )
    close_time = DateTimeField(
        null=True,
        blank=True,
        editable=False,
        help_text="Fecha y hora de cierre de la vela"
    )
    open_price = DecimalField(
        max_digits=20,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="Precio de apertura de la vela"
    )
    close_price = DecimalField(
        max_digits=20,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="Precio de cierre de la vela"
    )
    high_price = DecimalField(
        max_digits=20,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="Precio más alto de la vela"
    )
    low_price = DecimalField(
        max_digits=20,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="Precio más bajo de la vela"
    )
    volume = DecimalField(
        max_digits=30,
        decimal_places=10,
        help_text="Volumen de trading de la vela"
    )

    class Meta:
        db_table = 'candlesticks'

    def __str__(self):
        return f"{self.symbol} - {self.open_time}"
