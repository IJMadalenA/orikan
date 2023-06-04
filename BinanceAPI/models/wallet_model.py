from django.db.models import (
    CharField,
    DecimalField,
)

from BinanceAPI.models.base_binance_model import BaseBinanceModel


class Wallet(BaseBinanceModel):
    ASSET_CHOICES = (
        ('BTC', 'Bitcoin'),
        ('ETH', 'Ethereum'),
        # Agrega aquí más opciones de activos según tus necesidades
    )

    asset = CharField(
        max_length=10,
        choices=ASSET_CHOICES,
        help_text="Activo de la cartera"
    )
    free = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Saldo disponible"
    )
    locked = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Saldo bloqueado"
    )
    total = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Saldo total (disponible + bloqueado)"
    )

    class Meta:
        db_table = 'wallets'

    def __str__(self):
        return self.asset
