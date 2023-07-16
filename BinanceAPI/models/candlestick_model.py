from django.db.models import (
    ForeignKey,
    DateTimeField,
    DecimalField,
    CharField,
    CASCADE
)

from BinanceAPI.models.symbol_model import Symbol
from BinanceAPI.models.base_binance_model import BaseBinanceModel

TIME_FRAME_CHOICES = (
    ("1s", "1s"),
    ("1m", "1m"),
    ("3m", "3m"),
    ("5m", "5m"),
    ("15m", "15m"),
    ("30m", "30m"),
    ("1h", "1h"),
    ("2h", "2h"),
    ("4h", "4h"),
    ("6h", "6h"),
    ("8h", "8h"),
    ("12h", "12h"),
    ("1d", "1d"),
    ("3d", "3d"),
    ("5d", "5d"),
    ("1w", "1w"),
    ("2w", "2w"),
    ("3w", "3w"),
    ("1M", "1M"),
    ("3M", "3M"),
    ("6M", "6M"),
    ("1y", "1y"),
)


class Candlestick(BaseBinanceModel):
    symbol = ForeignKey(
        Symbol,
        on_delete=CASCADE,
        related_name='candlesticks',
        null=True,
        blank=True,
        editable=False,
        help_text="Símbolo del par de trading",
        verbose_name="Símbolo del par de trading",
    )
    time_frame = CharField(
        choices=TIME_FRAME_CHOICES,
        max_length=3,
        null=True,
        blank=True,
        editable=False,
        help_text="Marco de tiempo de la vela",
        verbose_name="Marco de tiempo de la vela",
    )
    open_time = DateTimeField(
        null=True,
        blank=True,
        editable=False,
        help_text="Fecha y hora de apertura de la vela",
        verbose_name="Fecha y hora de apertura de la vela",
    )
    open_price = DecimalField(
        max_digits=20,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="Precio de apertura de la vela",
        verbose_name="Precio de apertura de la vela",
    )
    high_price = DecimalField(
        max_digits=20,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="Precio más alto de la vela",
        verbose_name="Precio más alto de la vela",
    )
    low_price = DecimalField(
        max_digits=20,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="Precio más bajo de la vela",
        verbose_name="Precio más bajo de la vela",
    )
    close_price = DecimalField(
        max_digits=20,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="Precio de cierre de la vela",
        verbose_name="Precio de cierre de la vela",
    )
    adj_close_price = DecimalField(
        max_digits=20,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="Precio de cierre ajustado de la vela",
        verbose_name="Precio de cierre ajustado de la vela",
    )
    close_time = DateTimeField(
        null=True,
        blank=True,
        editable=False,
        help_text="Fecha y hora de cierre de la vela",
        verbose_name="Fecha y hora de cierre de la vela",
    )
    quote_asset_volume = DecimalField(
        max_digits=30,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="Volumen de trading en la vela",
        verbose_name="Volumen de trading en la vela",
    )
    number_of_trades = DecimalField(
        max_digits=30,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="Número de trades en la vela",
        verbose_name="Número de trades en la vela",
    )
    taker_buy_quote_asset_volume = DecimalField(
        max_digits=30,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="Volumen de trading de la vela",
        verbose_name="Volumen de trading de la vela",
    )
    taker_buy_base_asset_volume = DecimalField(
        max_digits=30,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="Volumen de trading de la vela",
        verbose_name="Volumen de trading de la vela",
    )
    volume = DecimalField(
        max_digits=30,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="Volumen de trading de la vela",
        verbose_name="Volumen de trading de la vela",
    )
    market_cap = DecimalField(
        max_digits=20,
        decimal_places=2,
        blank=False,
        null=False,
        editable=False,
        help_text="Capitalización de mercado",
        verbose_name="Capitalización de mercado",
    )

    class Meta:
        db_table = 'candlesticks'

    def __str__(self):
        return f"{self.symbol} - {self.open_time}"

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):

        # validate if symbol is not None.
        if self.symbol is None:
            raise ValueError("symbol must not be None.")

        # validate if open_time is not None or is not before than close_time.
        if self.open_time is None:
            raise ValueError("open_time must not be None.")
        elif self.close_time is not None and self.open_time > self.close_time:
            raise ValueError("open_time must be before than close_time.")

        # validate if open_price is not None and is not iqual or less than zero.
        if self.open_price is None or self.open_price <= 0:
            raise ValueError("open_price must be greater than zero.")

        # validate if high_price is not None and is not iqual or less than zero.
        if self.high_price is None or self.high_price <= 0:
            raise ValueError("high_price must be greater than zero.")

        # validate if low_price is not None and is not iqual or less than zero.
        if self.low_price is None or self.low_price <= 0:
            raise ValueError("low_price must be greater than zero.")

        # validate if close_price is not None and is not iqual or less than zero.
        if self.close_price is None or self.close_price <= 0:
            raise ValueError("close_price must be greater than zero.")

        # validate if adj_close_price is not None and is not iqual or less than zero.
        # If adj_close_price is None, then adj_close_price is equal to close_price.
        if self.adj_close_price is None:
            self.adj_close_price = self.close_price
        elif self.adj_close_price <= 0:
            raise ValueError("adj_close_price must be greater than zero.")

        # validate if volume is not None and is not iqual or less than zero.
        if self.volume is None or self.volume <= 0:
            raise ValueError("volume must be greater than zero.")

        self.market_cap = self.volume * self.close_price
        super().save(force_insert, force_update, using, update_fields)
