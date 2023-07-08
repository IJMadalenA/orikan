
from django.db.models import (
    ForeignKey,
    IntegerField,
    DecimalField,
    PROTECT,
    UniqueConstraint
)

from BinanceAPI.models.symbol_model import Symbol
from BinanceAPI.models.base_binance_model import BaseBinanceModel


class AvgPrice(BaseBinanceModel):
    """
    Este modelo se rellena a traves del método `get_avg_price()`.
    # https://python-binance.readthedocs.io/en/latest/binance.html?highlight=get_account_snapshot#binance.client.Client.get_avg_price
    """

    symbol = ForeignKey(
        Symbol,
        on_delete=PROTECT,
        max_length=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Activo",
    )
    mins = IntegerField(
        blank=False,
        null=False,
        editable=False,
        help_text="Minutos de los que se calcula el promedio",
    )
    price = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Precio promedio",
    )

    class Meta:
        # https://docs.djangoproject.com/en/4.2/ref/models/constraints/#uniqueconstraint
        constraints = [
            UniqueConstraint(
                fields=['symbol', 'mins'],
                name='unique_symbol_mins'
            )
        ]
        ordering = ['symbol', 'mins']
        verbose_name = "Precio promedio"
        verbose_name_plural = "Precios promedios"
