from django.db.models import (
    CharField,
    DecimalField,
    CASCADE,
    ForeignKey
)

from BinanceAPI.models import Account
from BinanceAPI.models.base_binance_model import BaseBinanceModel


class BalanceSpot(BaseBinanceModel):
    """
    Este modelo se rellena casi en su totalidad a traves
    del método `get_account_snapshot("SPOT")`.
    """
    ASSET_CHOICES = (
        ('BTC', 'Bitcoin'),
        ('ETH', 'Ethereum'),
        # Agrega aquí más opciones de activos según tus necesidades
    )
    account = ForeignKey(
        Account,
        on_delete=CASCADE
    )
    asset = CharField(
        # Siglas de la moneda, provisto por `get_account_snapshot("SPOT")`.
        max_length=10,
        choices=ASSET_CHOICES,
        blank=False,
        null=False,
        editable=False,
        help_text="Activo",
    )
    free = DecimalField(
        # Provisto por `get_account_snapshot("SPOT")`.
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Cantidad disponible",
    )
    locked = DecimalField(
        # Provisto por `get_account_snapshot("SPOT")`.
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Cantidad bloqueada",
    )
    total = DecimalField(
        # Provisto por `get_account_snapshot("SPOT")`.
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

    class Meta:
        db_table = 'balances'

    def __str__(self):
        return f"{self.asset}: Free: {self.free}, Locked: {self.locked}, Total: {self.total}"
