from django.core.exceptions import ValidationError
from django.db.models import (
    IntegerField,
    ForeignKey,
    CASCADE,
    DecimalField,
)

from BinanceAPI.models.symbol_model import Symbol
from BinanceAPI.models.base_binance_model import BaseBinanceModel


class Ticker(BaseBinanceModel):
    """

    """
    symbol = ForeignKey(
        Symbol,
        on_delete=CASCADE,
        related_name='ticker',
        related_query_name='ticker',
        blank=False,
        null=False,
        editable=False,
        help_text="Par de trading",
    )
    price = DecimalField(
        # get_symbol_ticket(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Precio actual",
    )
    price_change = DecimalField(
        # get_ticker(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Cambio de precio en 24 horas",
    )
    price_change_percent = DecimalField(
        # get_ticker(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Porcentaje de cambio de precio en 24 horas",
    )
    weighted_avg_price = DecimalField(
        # get_ticker(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Precio promedio ponderado",
    )
    prev_close_price = DecimalField(
        # get_ticker(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Precio de cierre anterior",
    )
    last_price = DecimalField(
        # get_ticker(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Último precio",
    )
    bid_price = DecimalField(
        # get_ticker(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Precio de oferta",
    )
    ask_price = DecimalField(
        # get_ticker(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Precio de demanda",
    )
    open_price = DecimalField(
        # get_ticker(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Precio de apertura",
    )
    high_price = DecimalField(
        # get_ticker(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Precio máximo",
    )
    low_price = DecimalField(
        # get_ticker(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Precio mínimo",
    )
    volume = DecimalField(
        # get_ticker(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Volumen",
    )
    open_time = IntegerField(
        # get_ticker(**params)
        blank=False,
        null=False,
        editable=False,
        help_text="Marca de tiempo de apertura",
    )
    close_time = IntegerField(
        # get_ticker(**params)
        blank=False,
        null=False,
        editable=False,
        help_text="Marca de tiempo de cierre",
    )
    first_trade_id = IntegerField(
        # get_ticker(**params)
        blank=False,
        null=False,
        editable=False,
        help_text="ID de la primera operación",
    )
    last_trade_id = IntegerField(
        # get_ticker(**params)
        blank=False,
        null=False,
        editable=False,
        help_text="ID de la última operación",
    )
    trade_count = IntegerField(
        # get_ticker(**params)
        blank=False,
        null=False,
        editable=False,
        help_text="Número de operaciones",
    )
    maker_commission = DecimalField(
        # get_trade_fee(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Comisión de maker",
    )
    taker_commission = DecimalField(
        # get_trade_fee(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Comisión de taker",
    )

    class Meta:
        verbose_name = "Ticker"
        verbose_name_plural = "Tickers"

    def clean_fields(self, exclude=None):
        try:
            if self.price < 0:
                raise ValidationError("El precio no puede ser negativo.")
            if self.close_time <= self.open_time:
                raise ValidationError("La marca de tiempo de cierre debe ser posterior a la marca de apertura.")
            if self.high_price < self.low_price:
                raise ValidationError("El precio máximo no puede ser menor al precio mínimo.")

        except Exception as e:
            raise ValidationError(e)

        super().clean_fields()

    def save(self, *args, **kwargs):
        try:
            self.full_clean()
            super().save(*args, **kwargs)
        except Exception as e:
            raise ValidationError("Error al guardar el ticker: " + str(e))

    def __str__(self):
        return self.symbol
