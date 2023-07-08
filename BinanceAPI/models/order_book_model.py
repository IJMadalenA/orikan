from django.db.models import (
    BigIntegerField,
    DateTimeField,
    ForeignKey,
    JSONField,
    DecimalField,
    CASCADE,
)

from BinanceAPI.models.base_binance_model import BaseBinanceModel
from BinanceAPI.models.asset_model import Asset


class OrderBook(BaseBinanceModel):
    asset = ForeignKey(
        Asset,
        on_delete=CASCADE,
        related_name='order_books',
        null=True,
        blank=True,
        editable=False,
        help_text="Símbolo del par de trading"
    )
    last_update_id = BigIntegerField(
        null=True,
        blank=True,
        editable=False,
        help_text="ID de última actualización del libro de órdenes"
    )
    timestamp = DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        editable=False,
        help_text="Fecha y hora de la actualización del libro de órdenes"
    )
    asks = JSONField(
        null=True,
        blank=True,
        editable=False,
        help_text="La lista de órdenes de venta (asks) del libro de órdenes."
    )
    bids = JSONField(
        null=True,
        blank=True,
        editable=False,
        help_text="La lista de órdenes de compra (bids) del libro de órdenes."
    )
    ask_total_volume = DecimalField(
        max_digits=20,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="El volumen total de las órdenes de venta."
    )
    bid_total_volume = DecimalField(
        max_digits=20,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="El volumen total de las órdenes de compra."
    )
    spread = DecimalField(
        max_digits=20,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="La diferencia entre el precio más alto de las órdenes de compra y el precio más bajo de las órdenes de venta."
    )
    liquidity = DecimalField(
        max_digits=20,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="La liquidez del par de trading."
    )
    depth = DecimalField(
        max_digits=20,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="La profundidad del libro de órdenes.",
    )

    class Meta:
        verbose_name = "Order Book"
        verbose_name_plural = "Order Books"
        db_table = 'order_books'

    def __str__(self):
        return f"{self.asset} - {self.timestamp}"
