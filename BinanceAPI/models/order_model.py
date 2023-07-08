from django.db.models import (
    CharField,
    DateTimeField,
    DecimalField,
)

from BinanceAPI.models.base_binance_model import BaseBinanceModel


class Order(BaseBinanceModel):
    SIDE_CHOICES = (
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
    )

    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('FILLED', 'Filled'),
        ('CANCELED', 'Canceled'),
    )

    asset = CharField(
        max_length=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Símbolo del activo",
        verbose_name="symbolo del activo",
    )
    order_id = CharField(
        db_index=True,
        max_length=50,
        unique=True,
        blank=False,
        null=False,
        editable=False,
        help_text="ID de la orden",
        verbose_name="ID de la orden",
    )
    price = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Precio de la orden",
        verbose_name="Precio de la orden",
    )
    quantity = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Cantidad de activos",
        verbose_name="Cantidad de activos",
    )
    side = CharField(
        max_length=4,
        choices=SIDE_CHOICES,
        blank=False,
        null=False,
        editable=False,
        help_text="Lado de la orden",
        verbose_name="Laso de la orden",
    )
    status = CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        blank=False,
        null=False,
        editable=False,
        help_text="Estado de la orden",
        verbose_name="Estado de la orden",
    )

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return self.order_id
