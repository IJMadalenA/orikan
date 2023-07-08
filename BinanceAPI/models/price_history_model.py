from django.db.models import (
    CASCADE,
    DateTimeField,
    DecimalField,
    ForeignKey,
)
from BinanceAPI.models.asset_model import Asset
from BinanceAPI.models.base_binance_model import BaseBinanceModel


class PriceHistory(BaseBinanceModel):
    asset = ForeignKey(
        Asset,
        on_delete=CASCADE,
        related_name='price_history',
        verbose_name='Criptomoneda',
    )
    timestamp = DateTimeField(
        blank=False,
        null=False,
        editable=False,
        help_text="Marca de tiempo del precio",
        verbose_name="Marce de tiempo del precio",
    )
    date_start = DateTimeField(
        blank=False,
        null=False,
        editable=False,
        help_text="Fecha de inicio",
        verbose_name="Fecha de inicio",
    )
    date_end = DateTimeField(
        blank=False,
        null=False,
        editable=False,
        help_text="Fecha de finalización",
        verbose_name="Fecha de finalización",
    )
    open_price = DecimalField(
        blank=False,
        null=False,
        editable=False,
        max_digits=20,
        decimal_places=10,
        help_text="Precio de apertura",
        verbose_name="Precio de apertura,",
    )
    high_price = DecimalField(
        blank=False,
        null=False,
        editable=False,
        max_digits=20,
        decimal_places=10,
        help_text="Precio máximo",
        verbose_name="Precio máximo",
    )
    low_price = DecimalField(
        blank=False,
        null=False,
        editable=False,
        max_digits=20,
        decimal_places=10,
        help_text="Precio mínimo",
        verbose_name="Precio mínimo",
    )
    close_price = DecimalField(
        blank=False,
        null=False,
        editable=False,
        max_digits=20,
        decimal_places=10,
        help_text="Precio de cierre",
        verbose_name="Precio de cierre",
    )
    volume = DecimalField(
        blank=False,
        null=False,
        editable=False,
        max_digits=20,
        decimal_places=10,
        help_text="Volumen de negociación",
        verbose_name="Volumen de negoción",
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
        db_table = 'price_history'
