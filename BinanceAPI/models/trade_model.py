from django.db.models import (
    CharField,
    DateTimeField,
    DecimalField,
    BooleanField,
    BigIntegerField,
)

from BinanceAPI.models.base_binance_model import BaseBinanceModel


class Trade(BaseBinanceModel):
    SIDE_CHOICES = (
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
    )

    trade_id = CharField(
        max_length=50,
        unique=True,
        blank=False,
        null=False,
        editable=False,
        help_text="ID de la operación",
    )
    asset = CharField(
        max_length=20,
        blank=False,
        null=False,
        editable=False,
        help_text="Símbolo de trading",
    )
    side = CharField(
        max_length=4,
        choices=SIDE_CHOICES,
        blank=False,
        null=False,
        editable=False,
        help_text="Lado de la operación (compra/venta)",
    )
    price = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Precio de la operación",
    )
    quantity = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Cantidad de la operación",
    )
    fee = DecimalField(
        max_digits=20,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="Comisión de la operación",
    )
    timestamp = DateTimeField(
        blank=False,
        null=False,
        editable=False,
        help_text="Fecha y hora de la operación",
    )
    is_maker = BooleanField(
        blank=False,
        null=False,
        editable=False,
        help_text="Indica si la operación fue creada por el maker"
    )
    is_buyer = BooleanField(
        blank=False,
        null=False,
        editable=False,
        help_text="Indica si el usuario es el comprador"
    )
    commission_asset = CharField(
        max_length=20,
        null=True,
        blank=True,
        editable=False,
        help_text="Símbolo de la comisión"
    )
    commission = DecimalField(
        max_digits=20,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="Monto de la comisión"
    )
    commission_rate = DecimalField(
        max_digits=20,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="Tasa de comisión"
    )
    buyer_fee = DecimalField(
        max_digits=20,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="Comisión del comprador"
    )
    seller_fee = DecimalField(
        max_digits=20,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="Comisión del vendedor"
    )
    trade_time = BigIntegerField(
        blank=False,
        null=False,
        editable=False,
        help_text="Tiempo de la operación en milisegundos"
    )
    buyer_is_maker = BooleanField(
        blank=False,
        null=False,
        editable=False,
        help_text="Indica si el comprador fue el maker"
    )
    ignore = BooleanField(
        blank=False,
        null=False,
        editable=False,
        help_text="Indica si la operación debe ignorarse"
    )

    class Meta:
        db_table = 'trades'

    def __str__(self):
        return self.trade_id
