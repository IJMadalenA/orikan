from _decimal import Decimal

from django.db.models import (
    ForeignKey,
    IntegerField,
    DecimalField,
    PROTECT,
    UniqueConstraint,
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

    def __str__(self):
        return f"{self.symbol} - {self.mins} mins"

    # https://docs.djangoproject.com/en/4.2/ref/models/instances/#django.db.models.Model.save
    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):

        # Validar que el campo `symbol` no sea nulo y luego que exista en la tabla `Symbol`.
        if self.symbol_id is None:
            raise ValueError(f"El campo `symbol` no puede ser nulo.")
        elif not Symbol.objects.filter(symbol=self.symbol).exists():
            raise ValueError(f"El campo `symbol` tiene que existir en la tabla `Symbol`.")

        # Validar que el campo `price` no sea nulo y luego que sea mayor a 0.
        if self.price is None:
            raise ValueError(f"El campo `price` no puede ser nulo.")
        elif self.price <= Decimal(0):
            raise ValueError(f"El campo `price` tiene que ser mayor a 0.")

        # Validar que el campo `mins` no sea nulo y luego que sea mayor a 0.
        if self.mins is None:
            raise ValueError(f"El campo `mins` no puede ser nulo.")
        elif self.mins <= 0:
            raise ValueError(f"El campo `mins` tiene que ser mayor a 0.")

        super().save(force_insert, force_update, using, update_fields)
