from django.db.models import (
    CharField,
    DecimalField,
)

from BinanceAPI.models.base_binance_model import BaseBinanceModel


class Balance(BaseBinanceModel):
    ASSET_CHOICES = (
        ('BTC', 'Bitcoin'),
        ('ETH', 'Ethereum'),
        # Agrega aquí más opciones de activos según tus necesidades
    )

    asset = CharField(
        max_length=10,
        choices=ASSET_CHOICES,
        blank=False,
        null=False,
        editable=False,
        help_text="Activo",
    )
    free = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Cantidad disponible",
    )
    locked = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Cantidad bloqueada",
    )
    total = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Cantidad total (free + locked)",
    )
    in_order = DecimalField(
        max_digits=20,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="Cantidad en órdenes abiertas"
    )
    btc_value = DecimalField(
        max_digits=20,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="Valor en BTC"
    )
    eth_value = DecimalField(
        max_digits=20,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="Valor en ETH"
    )

    class Meta:
        db_table = 'balances'

    def __str__(self):
        return f"{self.asset}: Free: {self.free}, Locked: {self.locked}, Total: {self.total}"
